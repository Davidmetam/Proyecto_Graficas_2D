import pygame
import sys
import math
import random
from figuras import Figuras
from animacion import Animacion
from hilos import Hilos

pygame.init()

ANCHO, ALTO = 800, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Proyecto Pac-Man")

try:
    background_image = pygame.image.load("pacmanmap.png").convert()
    background_image = pygame.transform.scale(background_image, (ANCHO, ALTO))
except pygame.error:
    sys.exit()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 26)
COLOR_BOLITAS_PACMAN = (255, 195, 99)
CIAN = (0, 255, 255)
ROSA = (255, 184, 222)
NARANJA = (255, 184, 82)


# --- Clases de Personajes ---

class Personaje:
    def __init__(self, x, y, velocidad=2):
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


class Pacman(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=3)
        self.angulo = 0
        self.direccion_deseada = (0, 0)

    def actualizar(self, eventos, grafo):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.direccion_deseada = (0, -1)
                elif evento.key == pygame.K_DOWN:
                    self.direccion_deseada = (0, 1)
                elif evento.key == pygame.K_LEFT:
                    self.direccion_deseada = (-1, 0)
                elif evento.key == pygame.K_RIGHT:
                    self.direccion_deseada = (1, 0)

        if self.nodo_actual == self.nodo_destino:
            vecinos = grafo.get(self.nodo_actual, [])
            for vecino in vecinos:
                if self.es_camino_valido(self.nodo_actual, vecino, self.direccion_deseada):
                    self.nodo_destino = vecino
                    self.direccion = self.direccion_deseada
                    break

        self.actualizar_angulo()
        self.mover()

    def es_camino_valido(self, nodo_inicio, nodo_fin, direccion):
        if direccion == (1, 0) and nodo_fin[0] > nodo_inicio[0]: return True
        if direccion == (-1, 0) and nodo_fin[0] < nodo_inicio[0]: return True
        if direccion == (0, 1) and nodo_fin[1] > nodo_inicio[1]: return True
        if direccion == (0, -1) and nodo_fin[1] < nodo_inicio[1]: return True
        return False

    def actualizar_angulo(self):
        if self.direccion == (1, 0):
            self.angulo = 0
        elif self.direccion == (-1, 0):
            self.angulo = 180
        elif self.direccion == (0, -1):
            self.angulo = 90
        elif self.direccion == (0, 1):
            self.angulo = 270

    def dibujar(self, dibujador, animacion):
        dibujar_pacman_abierto(self.x, self.y, self.angulo, dibujador, animacion)

    def reiniciar(self, x, y):
        self.x, self.y = x, y
        self.nodo_actual = (x, y)
        self.nodo_destino = (x, y)
        self.direccion = (0, 0)
        self.direccion_deseada = (0, 0)


class Fantasma(Personaje):
    def __init__(self, x, y, color):
        super().__init__(x, y, velocidad=10)
        self.color = color
        self.nodo_anterior = None

    def actualizar(self, grafo):
        if self.nodo_actual == self.nodo_destino:
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

    def dibujar(self, dibujador):
        dibujar_fantasma(self.x, self.y, self.color, dibujador)


# --- Funciones de Dibujo ---

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

    eye_radius, pupil_radius, eye_offset_x = radio / 2.5, radio / 5, radio / 2
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


# --- Lógica del Grafo y Colisiones ---

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


def verificar_colision(pacman, fantasmas):
    for fantasma in fantasmas:
        dist = math.sqrt((pacman.x - fantasma.x) ** 2 + (pacman.y - fantasma.y) ** 2)
        if dist < (pacman.radio + fantasma.radio) / 2:
            return True
    return False


# --- Inicialización del Juego ---

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

pacman_start_pos = (40, 40)
pacman = Pacman(pacman_start_pos[0], pacman_start_pos[1])

fantasmas = [
    Fantasma(270, 370, ROJO),
    Fantasma(350, 290, CIAN),
    Fantasma(270, 450, ROSA),
    Fantasma(350, 600, NARANJA)
]


# --- Bucle Principal del Juego ---
corriendo = True
reloj = pygame.time.Clock()
while corriendo:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            corriendo = False

    pacman.actualizar(eventos, grafo_caminos)
    for fantasma in fantasmas:
        fantasma.actualizar(grafo_caminos)

    if verificar_colision(pacman, fantasmas):
        pacman.reiniciar(pacman_start_pos[0], pacman_start_pos[1])

    ventana.blit(background_image, (0, 0))
    for x, y in coordenadas_puntos_comida:
        dibujar_puntos_comida(x, y, dibujador)
    for x, y in coordenadas_puntos_bonus:
        dibujar_puntos_bonus(x, y, dibujador)

    pacman.dibujar(dibujador, animacion)
    for fantasma in fantasmas:
        fantasma.dibujar(dibujador)

    pygame.display.update()
    reloj.tick(30)

pygame.quit()
sys.exit()