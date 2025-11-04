import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
import math

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Superficie Reloj de Arena 3D (Proyeccion Paralela)")
reloj = pygame.time.Clock()

Negro = (0,0,0)
BLANCO = (255, 255, 255)

dibujador = Figuras(ventana)
dibujador3D = Figuras3D(ventana)

centro_figura = (400, 300, 50)
escala_figura = 50
t_min_figura = -math.pi
t_max_figura = math.pi
pasos_t_figura = 50
pasos_phi_figura = 50

punto_de_proyeccion_figura = (0, 100, 300)

Corriendo = True

while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False

    ventana.fill(BLANCO)

    dibujador3D.dibujar_reloj_arena_superficie_proyectado(
        centro_figura,
        escala_figura,
        t_min_figura,
        t_max_figura,
        pasos_t_figura,
        pasos_phi_figura,
        punto_de_proyeccion_figura,
    )

    pygame.display.update()
    reloj.tick(60)

pygame.quit()