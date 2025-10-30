import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
from animacion import Animacion
from hilos_3d import Hilos3D

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Practicas ")
Negro ="#000000"
BLANCO=(255,255,255)
ROJO    = (255, 0, 0)
VERDE   = (0, 255, 0)
NARANJA=(255, 165, 0)
CIAN     = (0, 255, 255)
MORADO   = (128, 0, 128)
AZUL = (0, 0, 255)

dibujador = Figuras(ventana)
dibujador3D = Figuras3D(ventana)
animador = Animacion(ventana)
manejador_hilos_3d = Hilos3D(ventana)


Corriendo =True

punto_inicial_cubo = [355, 255, 50]
longitud_arista = 90
punto_de_fuga_cubo = [500, 400, 300]

vertices_cubo_base = dibujador3D.crear_cubo(punto_inicial_cubo, longitud_arista)

cx = punto_inicial_cubo[0] + longitud_arista / 2
cy = punto_inicial_cubo[1] + longitud_arista / 2
cz = punto_inicial_cubo[2] + longitud_arista / 2
centro_cubo = (cx, cy, cz)

aristas_cubo = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# manejador_hilos_3d.iniciar_traslacion_3d(tx_final=100, ty_final=50, tz_final=50, pasos=200)

# manejador_hilos_3d.iniciar_escalado_3d(sx_final=1.5, sy_final=1.5, sz_final=1.5, pasos=200)

# manejador_hilos_3d.iniciar_rotacion_x_3d(angulo_final=360, pasos=360)

#manejador_hilos_3d.iniciar_rotacion_y_3d(angulo_final=360, pasos=360)

manejador_hilos_3d.iniciar_rotacion_z_3d(angulo_final=360, pasos=360)


while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False
            manejador_hilos_3d.running = False

    ventana.fill(Negro)
    #dibujador.curva(100,50,300,170,150,ROJO)
    #dibujador.curva(8, 150, 300, 170, 150,ROJO)
    #dibujador.humito(150,300,400,50,40,ROJO)
    #dibujador.curva_parametricamente(100,100,400,50, ROJO)
    #dibujador.infinito(100,350,300,300,ROJO)
    #dibujador.mandala1(300,300,300,100,ROJO)
    #dibujador.mandala2(300,300,300,10,ROJO)

    #puntosX = [110, 120, 130, 140, 150, 160]
    #puntosY = [110, 120, 130, 140, 150, 160]
    #dibujador.mallado(puntosX, puntosY, ROJO)

    # punto_inicial_cubo = [392, 275, 50]
    # longitud_arista = 150
    # punto_proyeccion = [400, 300, 300]
    # dibujador3D.dibujar_cubo_proyectado(punto_inicial_cubo, longitud_arista, punto_proyeccion, ROJO)

    # punto_inicial_cubo = [355, 255, 50]
    # longitud_arista = 90
    # punto_de_fuga_cubo = [500, 400, 300]
    # dibujador.dibujar_pixel(punto_de_fuga_cubo[0], punto_de_fuga_cubo[1], AZUL)
    # dibujador3D.dibujar_cubo_fugado(punto_inicial_cubo, longitud_arista, punto_de_fuga_cubo, ROJO)

    # punto_inicial_piramide = [340, 380, 50]
    # longitud_base = 120
    # altura_piramide = 150
    # punto_de_fuga_piramide = [500, 300, 300]
    # dibujador.dibujar_pixel(punto_de_fuga_piramide[0], punto_de_fuga_piramide[1], AZUL)
    # dibujador3D.dibujar_piramide_fugada(punto_inicial_piramide, longitud_base, altura_piramide, punto_de_fuga_piramide, ROJO)

    vertices_transformados = []

    # with manejador_hilos_3d.lock_traslacion:
    #     tx, ty, tz = manejador_hilos_3d.tx, manejador_hilos_3d.ty, manejador_hilos_3d.tz
    # vertices_transformados = animador.traslacion_3d(vertices_cubo_base, tx, ty, tz)

    # with manejador_hilos_3d.lock_escalado:
    #     sx, sy, sz = manejador_hilos_3d.sx, manejador_hilos_3d.sy, manejador_hilos_3d.sz
    # vertices_transformados = animador.escalar_3d(vertices_cubo_base, sx, sy, sz, cx, cy, cz)

    # with manejador_hilos_3d.lock_rotacion_x:
    #     angulo_x = manejador_hilos_3d.angulo_x
    # vertices_transformados = animador.rotacion_x_3d(vertices_cubo_base, angulo_x, cx, cy, cz)

    # with manejador_hilos_3d.lock_rotacion_y:
    #     angulo_y = manejador_hilos_3d.angulo_y
    # vertices_transformados = animador.rotacion_y_3d(vertices_cubo_base, angulo_y, cx, cy, cz)

    with manejador_hilos_3d.lock_rotacion_z:
        angulo_z = manejador_hilos_3d.angulo_z
    vertices_transformados = animador.rotacion_z_3d(vertices_cubo_base, angulo_z, cx, cy, cz)

    dibujador.dibujar_pixel(punto_de_fuga_cubo[0], punto_de_fuga_cubo[1], AZUL)

    if vertices_transformados:
        dibujador3D._proyectar_y_dibujar_fugado(vertices_transformados, aristas_cubo, punto_de_fuga_cubo, ROJO)


    pygame.display.update()

pygame.quit()