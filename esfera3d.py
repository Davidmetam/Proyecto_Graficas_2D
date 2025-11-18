import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
from animacion import Animacion
from hilos_3d import Hilos3D

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dibujo Esfera")
reloj = pygame.time.Clock()

Negro = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (105, 163, 86)
verde_esfera=(61, 138, 6)

fondo = pygame.image.load("fondonav2.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))


dibujador = Figuras(ventana)
dibujador3D = Figuras3D(ventana)
animador = Animacion(ventana)
manejador_hilos_3d = Hilos3D(ventana)

punto_de_proyeccion_figura = (50, 50, 500)
centro_figura = (400, 300, 50)
radio = 100
pasos_theta = 40
pasos_phi = 40

vertices_base, caras_base = dibujador3D.crear_esfera_caras(
    centro_figura,
    radio,
    pasos_theta,
    pasos_phi
)

vertices_base = animador.rotacion_y_3d(vertices_base, 90, *centro_figura)
vertices_base = animador.rotacion_x_3d(vertices_base, 270, *centro_figura)

estado_animacion = "INICIAR_ROTAR_X"
vertices_actuales = vertices_base
vertices_transformados = vertices_base
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

    #ventana.fill(ROJO)
    ventana.blit(fondo, (0, 0))

    centro_actual = calcular_centro(vertices_actuales)

    if estado_animacion == "INICIAR_TRASLACION":
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
                estado_animacion = "INICIAR_ROTAR_X"

    elif estado_animacion == "FINALIZADO":
        vertices_transformados = vertices_actuales

    if vertices_transformados:
        dibujador3D._proyectar_y_dibujar_superficie(
            vertices_transformados,
            caras_base,
            punto_de_proyeccion_figura,
            verde_esfera
        )

    pygame.display.update()
    reloj.tick(60)

pygame.quit()