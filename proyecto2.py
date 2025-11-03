import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
import math

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dibujo Reloj de Arena 3D (Proyeccion Paralela)")
reloj = pygame.time.Clock()

Negro = "#000000"
ROJO = (255, 0, 0)

dibujador = Figuras(ventana)
dibujador3D = Figuras3D(ventana)

centro_figura = (ancho // 2, alto // 2, 50)
escala_figura = 50
t_min_figura = -math.pi
t_max_figura = math.pi
pasos_t_figura = 25
pasos_phi_figura = 25

punto_de_proyeccion_figura = (100, 100, 400)

Corriendo = True

while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False

    ventana.fill(Negro)

    dibujador3D.dibujar_reloj_arena_proyectado(
        centro_figura,
        escala_figura,
        t_min_figura,
        t_max_figura,
        pasos_t_figura,
        pasos_phi_figura,
        punto_de_proyeccion_figura,
        ROJO
    )

    pygame.display.update()
    reloj.tick(60)

pygame.quit()