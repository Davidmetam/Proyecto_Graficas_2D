import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
from animacion import Animacion
from hilos_3d import Hilos3D

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Animacion 3D Secuencial con Hilos")
reloj = pygame.time.Clock()

Negro = "#000000"
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
NARANJA = (255, 165, 0)
CIAN = (0, 255, 255)
MORADO = (128, 0, 128)
AZUL = (0, 0, 255)

dibujador = Figuras(ventana)
dibujador3D = Figuras3D(ventana)
animador = Animacion(ventana)
manejador_hilos_3d = Hilos3D(ventana)

punto_de_fuga_cubo = [500, 400, 300]
longitud_arista = 50


punto_inicial_cubo = [700, 265, 50]
vertices_base = dibujador3D.crear_cubo(punto_inicial_cubo, longitud_arista)

aristas_cubo = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

estado_animacion = "INICIAR_TRASLACION"
vertices_actuales = vertices_base
vertices_transformados = vertices_base
color_actual = ROJO

PASOS_ANIMACION = 150


def calcular_centro(vertices):
    x_sum = sum(v[0] for v in vertices)
    y_sum = sum(v[1] for v in vertices)
    z_sum = sum(v[2] for v in vertices)
    num_vertices = len(vertices)
    return (x_sum / num_vertices, y_sum / num_vertices, z_sum / num_vertices)


Corriendo = True
while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False
            manejador_hilos_3d.running = False

    ventana.fill(Negro)

    centro_actual = calcular_centro(vertices_actuales)

    if estado_animacion == "INICIAR_TRASLACION":
        color_actual = ROJO
        manejador_hilos_3d.iniciar_traslacion_3d(tx_final=-350, ty_final=0, tz_final=0, pasos=PASOS_ANIMACION)
        estado_animacion = "DIBUJAR_TRASLACION"

    elif estado_animacion == "DIBUJAR_TRASLACION":
        with manejador_hilos_3d.lock_traslacion:
            tx, ty, tz = manejador_hilos_3d.tx, manejador_hilos_3d.ty, manejador_hilos_3d.tz
        vertices_transformados = animador.traslacion_3d(vertices_base, tx, ty, tz)

        if not manejador_hilos_3d.hilo_traslacion.is_alive():
            if manejador_hilos_3d.tx == -350:
                vertices_actuales = vertices_transformados
                vertices_base = vertices_actuales
                estado_animacion = "INICIAR_ESCALADO"

    elif estado_animacion == "INICIAR_ESCALADO":
        color_actual = VERDE
        manejador_hilos_3d.iniciar_escalado_3d(sx_final=2.0, sy_final=2.0, sz_final=2.0, pasos=PASOS_ANIMACION)
        estado_animacion = "DIBUJAR_ESCALADO"

    elif estado_animacion == "DIBUJAR_ESCALADO":
        with manejador_hilos_3d.lock_escalado:
            sx, sy, sz = manejador_hilos_3d.sx, manejador_hilos_3d.sy, manejador_hilos_3d.sz
        vertices_transformados = animador.escalar_3d(vertices_base, sx, sy, sz, *centro_actual)

        if not manejador_hilos_3d.hilo_escalado.is_alive():
            if manejador_hilos_3d.sx == 2.0:
                vertices_actuales = vertices_transformados
                vertices_base = vertices_actuales
                estado_animacion = "INICIAR_ROTAR_X"

    elif estado_animacion == "INICIAR_ROTAR_X":
        color_actual = CIAN
        manejador_hilos_3d.iniciar_rotacion_x_3d(angulo_final=360, pasos=PASOS_ANIMACION)
        estado_animacion = "DIBUJAR_ROTAR_X"

    elif estado_animacion == "DIBUJAR_ROTAR_X":
        with manejador_hilos_3d.lock_rotacion_x:
            angulo_x = manejador_hilos_3d.angulo_x
        vertices_transformados = animador.rotacion_x_3d(vertices_base, angulo_x, *centro_actual)

        if not manejador_hilos_3d.hilo_rotacion_x.is_alive():
            if manejador_hilos_3d.angulo_x == 360:
                vertices_actuales = vertices_transformados
                vertices_base = vertices_actuales
                estado_animacion = "INICIAR_ROTAR_Y"

    elif estado_animacion == "INICIAR_ROTAR_Y":
        color_actual = MORADO
        manejador_hilos_3d.iniciar_rotacion_y_3d(angulo_final=360, pasos=PASOS_ANIMACION)
        estado_animacion = "DIBUJAR_ROTAR_Y"

    elif estado_animacion == "DIBUJAR_ROTAR_Y":
        with manejador_hilos_3d.lock_rotacion_y:
            angulo_y = manejador_hilos_3d.angulo_y
        vertices_transformados = animador.rotacion_y_3d(vertices_base, angulo_y, *centro_actual)

        if not manejador_hilos_3d.hilo_rotacion_y.is_alive():
            if manejador_hilos_3d.angulo_y == 360:
                vertices_actuales = vertices_transformados
                vertices_base = vertices_actuales
                estado_animacion = "INICIAR_ROTAR_Z"

    elif estado_animacion == "INICIAR_ROTAR_Z":
        color_actual = NARANJA
        manejador_hilos_3d.iniciar_rotacion_z_3d(angulo_final=360, pasos=PASOS_ANIMACION)
        estado_animacion = "DIBUJAR_ROTAR_Z"

    elif estado_animacion == "DIBUJAR_ROTAR_Z":
        with manejador_hilos_3d.lock_rotacion_z:
            angulo_z = manejador_hilos_3d.angulo_z
        vertices_transformados = animador.rotacion_z_3d(vertices_base, angulo_z, *centro_actual)

        if not manejador_hilos_3d.hilo_rotacion_z.is_alive():
            if manejador_hilos_3d.angulo_z == 360:
                vertices_actuales = vertices_transformados
                vertices_base = vertices_actuales
                estado_animacion = "FINALIZADO"

    elif estado_animacion == "FINALIZADO":
        vertices_transformados = vertices_actuales

    dibujador.dibujar_pixel(punto_de_fuga_cubo[0], punto_de_fuga_cubo[1], AZUL)

    if vertices_transformados:
        dibujador3D._proyectar_y_dibujar_fugado(vertices_transformados, aristas_cubo, punto_de_fuga_cubo, color_actual)

    pygame.display.update()
    reloj.tick(60)

pygame.quit()