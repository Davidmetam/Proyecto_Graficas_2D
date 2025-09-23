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

def dibujar_pacman_abierto(x, y, color=AMARILLO):
    return 0

def dibujar_pacman_cerrado(x, y):
    dibujador.activar_relleno(AMARILLO)
    dibujador.dibujar_circulo_coordenadas_polares(x, y, 20, AMARILLO)
    dibujador.desactivar_relleno()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    #ventana.fill(NEGRO)
    ventana.blit(background_image, (0, 0))

    #ancho de paredes = 40
    dibujador.dibujar_linea_dda(100,20,100,60,AMARILLO)
    dibujar_pacman_cerrado(30, 30)

    pygame.display.update()

pygame.quit()
sys.exit()