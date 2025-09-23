import pygame
import sys
import math
import random
from figuras import Figuras
from animacion import Animacion

pygame.init()

ANCHO, ALTO = 800, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Proyecto pacman")

try:
    background_image = pygame.image.load("pacmanmap.png").convert()
    background_image = pygame.transform.scale(background_image, (ANCHO, ALTO))
except pygame.error:
    sys.exit()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (50, 50, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 26)
COLOR_BOLITAS_PACMAN = (255, 195, 99)
CIAN = (0, 255, 255)
ROSA = (255, 184, 222)
NARANJA = (255, 184, 82)
SELECTOR = 1

class Personaje:
    def __init__(self, x, y, velocidad=2):
        self.start_x, self.start_y = x, y
        self.x, self.y = x, y
        self.velocidad = velocidad
        self.nodo_actual = (x, y)
        self.nodo_destino = (x, y)
        self.direccion = (0, 0)
        self.radio = 15

    def mover(self):
        if self.nodo_actual == self.nodo_destino:
            return

        for _ in range(self.velocidad):
            if self.nodo_actual == self.nodo_destino:
                break

            self.x += self.direccion[0] * 1
            self.y += self.direccion[1] * 1

            overshot = False
            if self.direccion[0] > 0 and self.x >= self.nodo_destino[0]:
                overshot = True
            elif self.direccion[0] < 0 and self.x <= self.nodo_destino[0]:
                overshot = True
            elif self.direccion[1] > 0 and self.y >= self.nodo_destino[1]:
                overshot = True
            elif self.direccion[1] < 0 and self.y <= self.nodo_destino[1]:
                overshot = True

            if overshot:
                self.x, self.y = self.nodo_destino
                self.nodo_actual = self.nodo_destino

    def reiniciar(self):
        self.x, self.y = self.start_x, self.start_y
        self.nodo_actual = (self.start_x, self.start_y)
        self.nodo_destino = (self.start_x, self.start_y)
        self.direccion = (0, 0)

class Pacman(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=31)
        self.SELECTOR = 1
        self.angulo = 0
        self.nodo_anterior = None

    def actualizar(self, grafo):
        if self.nodo_actual == self.nodo_destino:
            if self.nodo_actual == (40, 370):
                self.x, self.y = 760, 370
                self.nodo_actual = (self.x, self.y)
                self.nodo_destino = (620, 370)
            elif self.nodo_actual == (760, 370):
                self.x, self.y = 40, 370
                self.nodo_actual = (self.x, self.y)
                self.nodo_destino = (180, 370)
            else:
                vecinos = grafo.get(self.nodo_actual, [])
                opciones = [vecino for vecino in vecinos if vecino != self.nodo_anterior]
                if not opciones:
                    opciones = vecinos

                self.nodo_anterior = self.nodo_actual
                self.nodo_destino = random.choice(opciones)

            dist_x = self.nodo_destino[0] - self.nodo_actual[0]
            dist_y = self.nodo_destino[1] - self.nodo_actual[1]

            if dist_x != 0:
                self.direccion = (1 if dist_x > 0 else -1, 0)
            elif dist_y != 0:
                self.direccion = (0, 1 if dist_y > 0 else -1)

        self.actualizar_angulo()
        self.mover()

    def actualizar_angulo(self):
        if self.direccion == (1, 0):
            self.angulo = 0
        elif self.direccion == (-1, 0):
            self.angulo = 180
        elif self.direccion == (0, -1):
            self.angulo = 270
        elif self.direccion == (0, 1):
            self.angulo = 90

    def dibujar(self, dibujador, animacion):
        if self.SELECTOR > 0:
            dibujar_pacman_abierto(self.x, self.y, self.angulo, dibujador, animacion)
            self.SELECTOR *= -1
        else:
            dibujar_pacman(self.x, self.y)
            self.SELECTOR *= -1

class Fantasma(Personaje):
    def __init__(self, x, y, color):
        super().__init__(x, y, velocidad=30)
        self.color_original = color
        self.color = color
        self.nodo_anterior = None
        self.estado = 'normal'

    def actualizar(self, grafo):
        if self.nodo_actual == self.nodo_destino:
            if self.nodo_actual == (40, 370):
                self.x, self.y = 760, 370
                self.nodo_actual = (self.x, self.y)
                self.nodo_destino = (620, 370)
            elif self.nodo_actual == (760, 370):
                self.x, self.y = 40, 370
                self.nodo_actual = (self.x, self.y)
                self.nodo_destino = (180, 370)
            else:
                vecinos = grafo.get(self.nodo_actual, [])
                opciones = [vecino for vecino in vecinos if vecino != self.nodo_anterior]
                if not opciones:
                    opciones = vecinos

                self.nodo_anterior = self.nodo_actual
                self.nodo_destino = random.choice(opciones)

            dist_x = self.nodo_destino[0] - self.nodo_actual[0]
            dist_y = self.nodo_destino[1] - self.nodo_actual[1]

            if dist_x != 0:
                self.direccion = (1 if dist_x > 0 else -1, 0)
            elif dist_y != 0:
                self.direccion = (0, 1 if dist_y > 0 else -1)

        self.mover()

    def set_vulnerable(self, es_vulnerable):
        if es_vulnerable:
            self.estado = 'vulnerable'
            self.color = AZUL
        else:
            self.estado = 'normal'
            self.color = self.color_original

    def dibujar(self, dibujador):
        dibujar_fantasma(self.x, self.y, self.color, dibujador)

def dibujar_pacman_abierto(x, y, angulo_rotacion, dibujador, animacion):
    vertices = []
    vertices.append((x, y))
    for i in range(45, 360 - 45 + 1):
        angulo = math.radians(i)
        punto_x = x + 20 * math.cos(angulo)
        punto_y = y - 20 * math.sin(angulo)
        vertices.append((punto_x, punto_y))

    pacman_rotado = animacion.rotar(vertices, angulo_rotacion, x, y)
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_poligono(pacman_rotado, AMARILLO)
    dibujador.desactivar_relleno()

def dibujar_pacman(x, y):
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 20, AMARILLO)
    dibujador.desactivar_relleno()

def dibujar_fantasma(x, y, color, dibujador):
    radio = 18
    vertices = []
    for i in range(180, 361):
        angulo = math.radians(i)
        vertices.append((x + radio * math.cos(angulo), y - radio * math.sin(angulo)))
    vertices.extend([(x + radio, y + radio), (x + radio / 1.5, y + radio + radio / 2), (x, y + radio),
                     (x - radio / 1.5, y + radio + radio / 2), (x - radio, y + radio)])

    dibujador.activar_relleno(color)
    dibujador.dibujar_poligono(vertices, color)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, radio, color)
    dibujador.desactivar_relleno()

    eye_radius, pupil_radius, eye_offset_x = radio / 3, radio / 6, radio / 2
    for sign in [-1, 1]:
        eye_x = x + eye_offset_x * sign
        dibujador.activar_relleno(BLANCO)
        dibujador.dibujar_circulo_coordenadas_polares(eye_x, y, eye_radius, BLANCO)
        dibujador.desactivar_relleno()
        dibujador.activar_relleno(NEGRO)
        dibujador.dibujar_circulo_coordenadas_polares(eye_x, y, pupil_radius, NEGRO)
        dibujador.desactivar_relleno()

def dibujar_puntos_comida(x, y, dibujador):
    dibujador.activar_relleno(BLANCO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 3, BLANCO)
    dibujador.desactivar_relleno()

def dibujar_puntos_bonus(x, y, dibujador):
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 10, AMARILLO)
    dibujador.desactivar_relleno()

def construir_grafo(segmentos):
    grafo = {}

    def agregar_conexion(p1, p2):
        if p1 not in grafo: grafo[p1] = []
        if p2 not in grafo: grafo[p2] = []
        if p2 not in grafo[p1]: grafo[p1].append(p2)
        if p1 not in grafo[p2]: grafo[p2].append(p1)

    for p1, p2 in segmentos:
        agregar_conexion(p1, p2)
    return grafo

def reiniciar_juego():
    pacman.reiniciar()
    for fantasma in fantasmas:
        fantasma.reiniciar()
        fantasma.set_vulnerable(False)

dibujador = Figuras(ventana)
animacion = Animacion(ventana)

caminos_laterales = [(40, 40, 180, 40), (180, 40, 350, 40), (40, 40, 40, 140), (40, 140, 40, 220), (40, 220, 180, 220),
                     (350, 40, 350, 140), (40, 140, 180, 140), (180, 140, 270, 140), (270, 140, 350, 140),
                     (270, 140, 270, 220), (270, 220, 350, 220), (350, 220, 350, 290), (350, 290, 270, 290),
                     (270, 290, 270, 370), (270, 370, 180, 370), (180, 370, 40, 370), (270, 370, 270, 450),
                     (270, 450, 270, 530), (270, 530, 180, 530), (180, 530, 40, 530), (40, 530, 40, 600),
                     (40, 600, 90, 600), (90, 600, 90, 680), (90, 680, 180, 680), (90, 680, 40, 680),
                     (40, 680, 40, 760), (40, 760, 350, 760), (350, 760, 350, 680), (350, 680, 270, 680),
                     (270, 680, 270, 600), (270, 600, 180, 600), (270, 600, 350, 600), (350, 600, 350, 530),
                     (350, 530, 270, 530), (180, 40, 180, 140), (180, 140, 180, 220), (180, 220, 180, 370),
                     (180, 370, 180, 530), (180, 530, 180, 600), (180, 600, 180, 680)]
caminos_centrales = [(350, 140, 450, 140), (350, 290, 450, 290), (350, 600, 450, 600), (350, 760, 450, 760),
                     (270, 450, 530, 450)]

segmentos_del_mapa = []
for x1, y1, x2, y2 in caminos_laterales:
    segmentos_del_mapa.append(((x1, y1), (x2, y2)))
    segmentos_del_mapa.append(((ANCHO - x1, y1), (ANCHO - x2, y2)))
for x1, y1, x2, y2 in caminos_centrales:
    segmentos_del_mapa.append(((x1, y1), (x2, y2)))

grafo_caminos = construir_grafo(segmentos_del_mapa)

coordenadas_puntos_bonus = [(40, 40), (760, 40), (40, 680), (760, 680)]
coordenadas_puntos_comida = set()
for p1, p2 in segmentos_del_mapa:
    x1, y1 = p1;
    x2, y2 = p2
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2), 30): coordenadas_puntos_comida.add((x, y1))
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2), 30): coordenadas_puntos_comida.add((x1, y))

pacman_start_pos = (180, 40)
pacman = Pacman(pacman_start_pos[0], pacman_start_pos[1])
fantasmas = [
    Fantasma(760, 40, ROJO),
    Fantasma(760, 680, CIAN),
    Fantasma(270, 450, ROSA),
    Fantasma(40, 680, NARANJA)
]

bonus_activo = False
bonus_timer = 0
DURACION_BONUS = 30000

corriendo = True
reloj = pygame.time.Clock()
while corriendo:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            corriendo = False

    pacman.actualizar(grafo_caminos)
    for fantasma in fantasmas:
        fantasma.actualizar(grafo_caminos)

    punto_comido = None
    for punto in coordenadas_puntos_comida:
        dist = math.sqrt((pacman.x - punto[0]) ** 2 + (pacman.y - punto[1]) ** 2)
        if dist < pacman.radio:
            punto_comido = punto
            break
    if punto_comido:
        coordenadas_puntos_comida.remove(punto_comido)

    bonus_comido = None
    for punto in coordenadas_puntos_bonus:
        dist = math.sqrt((pacman.x - punto[0]) ** 2 + (pacman.y - punto[1]) ** 2)
        if dist < pacman.radio:
            bonus_comido = punto
            break
    if bonus_comido:
        coordenadas_puntos_bonus.remove(bonus_comido)
        bonus_activo = True
        bonus_timer = pygame.time.get_ticks()
        for fantasma in fantasmas:
            fantasma.set_vulnerable(True)

    if bonus_activo and pygame.time.get_ticks() - bonus_timer > DURACION_BONUS:
        bonus_activo = False
        for fantasma in fantasmas:
            fantasma.set_vulnerable(False)

    for fantasma in fantasmas:
        dist = math.sqrt((pacman.x - fantasma.x) ** 2 + (pacman.y - fantasma.y) ** 2)
        if dist < pacman.radio + fantasma.radio:
            if fantasma.estado == 'vulnerable':
                fantasma.reiniciar()
            else:
                reiniciar_juego()
            break

    ventana.blit(background_image, (0, 0))
    for x, y in coordenadas_puntos_comida:
        dibujar_puntos_comida(x, y, dibujador)
    for x, y in coordenadas_puntos_bonus:
        dibujar_puntos_bonus(x, y, dibujador)

    pacman.dibujar(dibujador, animacion)
    for fantasma in fantasmas:
        fantasma.dibujar(dibujador)

    pygame.display.update()
    reloj.tick(300)

pygame.quit()
sys.exit()