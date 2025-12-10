import pygame
from figuras import Figuras
from figuras_3d import Figuras3D
from animacion import Animacion
from hilos_3d import Hilos3D
import random
import time
import math

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Esfera Navideña Animada con Iluminación")
reloj = pygame.time.Clock()

Negro = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (105, 163, 86)
verde_esfera = (61, 138, 6)
COLOR_ESTRELLA_RELLENO = (255, 255, 0)
COLOR_ESTRELLA_BORDE = (245, 187, 39)
PUNTO_PROYECCION_ESTRELLA = (0, 0, 10)

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

luz_base_x = 400
luz_base_y = 200
luz_base_z = 300
angulo_luz = 0

vertices_base, caras_base = dibujador3D.crear_esfera_caras_navideña(
    centro_figura,
    radio,
    pasos_theta,
    pasos_phi,
    tiempo=0
)

vertices_base = animador.rotacion_y_3d(vertices_base, 90, *centro_figura)
vertices_base = animador.rotacion_x_3d(vertices_base, 270, *centro_figura)

estado_animacion = "INICIAR_ROTAR_X"
vertices_actuales = vertices_base
vertices_transformados = vertices_base
PASOS_ANIMACION = 150

tiempo_inicio = time.time()


def calcular_centro(vertices):
    x_sum = sum(v[0] for v in vertices)
    y_sum = sum(v[1] for v in vertices)
    z_sum = sum(v[2] for v in vertices)
    n = len(vertices)
    if n == 0:
        return (0, 0, 0)
    return (x_sum / n, y_sum / n, z_sum / n)

estrellas_data = [
    (700, 200, 30, 35),
    (500, 150, 60, 25),
    (350, 500, 80, 35),
    (700, 400, 50, 25),
    (450, 500, 40, 20),
    (650, 250, 90, 30),
    (650, 520, 20, 50),
    (350, 100, 70, 22),
    (200, 150, 40, 33),
    (550, 400, 60, 28)
]

estrellas_data.sort(key=lambda s: s[3])

estrellas_animadas = []

for i in range(len(estrellas_data)):
    x, y, z, s = estrellas_data[i]
    centro = (x, y, z)
    vertices, caras = dibujador3D.crear_estrella_3d(centro, s)
    manager = Hilos3D(ventana)

    anim_type = ''
    if i < 3:
        anim_type = 'scale'
        manager.iniciar_escalado_ciclico_3d(escala_max=1.8, pasos_ciclo=100 + i * 20)
    elif i < 6:
        anim_type = 'rot_z'
        manager.iniciar_rotacion_z_continua_3d(velocidad=1.0 + (i * 0.4))
    else:
        anim_type = 'rot_x'
        manager.iniciar_rotacion_x_continua_3d(velocidad=0.8 + (i * 0.2))

    estrellas_animadas.append({
        'centro': centro,
        'vertices_base': vertices,
        'caras': caras,
        'manager': manager,
        'anim_type': anim_type
    })

Corriendo = True
while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False
            manejador_hilos_3d.running = False
            for estrella in estrellas_animadas:
                estrella['manager'].running = False

    ventana.blit(fondo, (0, 0))

    tiempo_actual = time.time() - tiempo_inicio

    angulo_luz += 0.02
    radio_luz = 200
    luz_x = luz_base_x + radio_luz * math.cos(angulo_luz)
    luz_y = luz_base_y + radio_luz * math.sin(angulo_luz)
    luz_z = luz_base_z
    luz_pos = (luz_x, luz_y, luz_z)

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

    if vertices_transformados:
        dibujador3D._proyectar_y_dibujar_superficie_con_iluminacion(
            vertices_transformados,
            caras_base,
            punto_de_proyeccion_figura,
            luz_pos,
            usar_textura=True,
            tiempo=tiempo_actual
        )

    for estrella in estrellas_animadas:
        v_base = estrella['vertices_base']
        centro = estrella['centro']
        caras = estrella['caras']
        manager = estrella['manager']
        v_transformados = v_base

        if estrella['anim_type'] == 'scale':
            with manager.lock_escalado:
                sx, sy, sz = manager.sx, manager.sy, manager.sz
            v_transformados = animador.escalar_3d(v_base, sx, sy, sz, *centro)

        elif estrella['anim_type'] == 'rot_z':
            with manager.lock_rotacion_z:
                angulo_z = manager.angulo_z
            v_transformados = animador.rotacion_z_3d(v_base, angulo_z, *centro)

        elif estrella['anim_type'] == 'rot_x':
            with manager.lock_rotacion_x:
                angulo_x = manager.angulo_x
            v_transformados = animador.rotacion_y_3d(v_base, angulo_x, *centro)

        dibujador3D.dibujar_estrella_3d_con_brillo(
            v_transformados,
            caras,
            PUNTO_PROYECCION_ESTRELLA,
            luz_pos,
            tiempo=tiempo_actual
        )

    pygame.display.update()
    reloj.tick(60)

pygame.quit()