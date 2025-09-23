import math

import pygame
import sys
from figuras import Figuras
from animacion import Animacion
from hilos import Hilos

pygame.init()

ANCHO, ALTO = 800, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Proyecto primer parcial")

try:
    background_image = pygame.image.load("pacmanmap.png").convert()
    background_image = pygame.transform.scale(background_image, (ANCHO, ALTO))
except pygame.error:
    print("Error: No se pudo cargar la imagen de fondo 'fondo.jpg'.")
    print("Asegúrate de que el archivo existe en el mismo directorio que el script.")
    sys.exit()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255,255,26)
COLOR_BOLITAS_PACMAN=(255,195,99)

dibujador = Figuras(ventana)
animacion = Animacion(ventana)
hilos = Hilos(ventana)

def dibujar_pacman_abierto(x, y, angulo_rotacion):
    color = AMARILLO
    radio = 20
    angulo_boca = 45

    vertices = []
    vertices.append((x, y))

    for i in range(angulo_boca, 360 - angulo_boca + 1):
        angulo = math.radians(i)
        punto_x = x + radio * math.cos(angulo)
        punto_y = y - radio * math.sin(angulo)
        vertices.append((punto_x, punto_y))

    pacman_rotado = animacion.rotar(vertices, angulo_rotacion, x, y)
    dibujador.activar_relleno(color)
    dibujador.dibujar_poligono(pacman_rotado, color)
    dibujador.desactivar_relleno()

def dibujar_pacman_cerrado(x, y):
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 20, AMARILLO)
    dibujador.desactivar_relleno()

def dibujar_puntos_comida(x, y):
    dibujador.activar_relleno(BLANCO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 3, BLANCO)
    dibujador.desactivar_relleno()

def dibujar_puntos_bonus(x, y):
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 10, COLOR_BOLITAS_PACMAN)
    dibujador.desactivar_relleno()

def dibujar_fantasma(x, y, color):
    radio = 18
    vertices = []

    for i in range(180, 361):
        angulo = math.radians(i)
        punto_x = x + radio * math.cos(angulo)
        punto_y = y - radio * math.sin(angulo)
        vertices.append((punto_x, punto_y))

    vertices.append((x + radio, y + radio))
    vertices.append((x + radio / 1.5, y + radio + radio / 2))
    vertices.append((x, y + radio))
    vertices.append((x - radio / 1.5, y + radio + radio / 2))
    vertices.append((x - radio, y + radio))

    dibujador.activar_relleno(color)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 18, color)
    dibujador.dibujar_poligono(vertices, color)
    dibujador.desactivar_relleno()

    eye_radius = radio / 2.5
    pupil_radius = eye_radius / 2
    eye_offset_x = radio / 2
    eye_y = y

    left_eye_x = x - eye_offset_x
    dibujador.activar_relleno(BLANCO)
    dibujador.dibujar_circulo_coordenadas_polares(left_eye_x, eye_y, eye_radius, BLANCO)
    dibujador.desactivar_relleno()
    dibujador.activar_relleno(NEGRO)
    dibujador.dibujar_circulo_coordenadas_polares(left_eye_x, eye_y, pupil_radius, NEGRO)
    dibujador.desactivar_relleno()

    right_eye_x = x + eye_offset_x
    dibujador.activar_relleno(BLANCO)
    dibujador.dibujar_circulo_coordenadas_polares(right_eye_x, eye_y, eye_radius, BLANCO)
    dibujador.desactivar_relleno()
    dibujador.activar_relleno(NEGRO)
    dibujador.dibujar_circulo_coordenadas_polares(right_eye_x, eye_y, pupil_radius, NEGRO)
    dibujador.desactivar_relleno()

caminos_laterales = [
    (40 , 40 , 180, 40 ), (180, 40 , 350, 40 ), (40 , 40 , 40 , 140),
    (40 , 140, 40 , 220), (40 , 220, 180, 220), (350, 40 , 350, 140),
    (40 , 140, 180, 140), (180, 140, 270, 140), (270, 140, 350, 140),
    (270, 140, 270, 220), (270, 220, 350, 220), (350, 220, 350, 290),
    (350, 290, 270, 290), (270, 290, 270, 370), (270, 370, 180, 370),
    (180, 370, 0  , 370), (270, 370, 270, 450), (270, 450, 270, 530),
    (270, 530, 180, 530), (180, 530, 40 , 530), (40 , 530, 40 , 600),
    (40 , 600, 90 , 600), (90 , 600, 90 , 680), (90 , 680, 180, 680),
    (90 , 680, 40 , 680), (40 , 680, 40 , 760), (40 , 760, 350, 760),
    (350, 760, 350, 680), (350, 680, 270, 680), (270, 680, 270, 600),
    (270, 600, 180, 600), (270, 600, 350, 600), (350, 600, 350, 530),
    (350, 530, 270, 530), (180, 40 , 180, 140), (180, 140, 180, 220),
    (180, 220, 180, 370), (180, 370, 180, 530), (180, 530, 180, 600),
    (180, 600, 180, 680),
]

caminos_centrales = [
    (350, 140, 450, 140), (350, 290, 450, 290),
    (350, 600, 450, 600), (350, 760, 450, 760),
    (270, 450, 530, 450)
]

coordenadas_puntos_bonus = [
    (40, 40), (760, 40), (40, 680), (760, 680)
]

coordenadas_puntos_comida = set()
distancia_entre_puntos = 30

for x1, y1, x2, y2 in caminos_laterales:
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2), distancia_entre_puntos):
            if x > 0: coordenadas_puntos_comida.add((x, y1))
            if (ANCHO - x) < ANCHO: coordenadas_puntos_comida.add((ANCHO - x, y1))
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2), distancia_entre_puntos):
            coordenadas_puntos_comida.add((x1, y))
            coordenadas_puntos_comida.add((ANCHO - x1, y))

for x1, y1, x2, y2 in caminos_centrales:
    if y1 == y2:
        for x in range(x1, x2, distancia_entre_puntos):
            coordenadas_puntos_comida.add((x, y1))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False


    ventana.blit(background_image, (0, 0))

    for x, y in coordenadas_puntos_comida:
        dibujar_puntos_comida(x, y)

    for x, y in coordenadas_puntos_bonus:
        dibujar_puntos_bonus(x, y)

    pygame.display.update()

pygame.quit()
sys.exit()