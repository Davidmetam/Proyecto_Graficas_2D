import math
import collections


class Figuras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.relleno_activo = False
        self.color_relleno = (0, 0, 0)
        self.metodo_relleno = 'scanline'

    def activar_relleno(self, color, metodo='scanline'):
        self.relleno_activo = True
        self.color_relleno = color
        self.metodo_relleno = metodo

    def desactivar_relleno(self):
        self.relleno_activo = False

    def dibujar_pixel(self, x, y, color):
        self.ventana.set_at((round(x), round(y)), color)

    def dibujar_linea_dda(self, x_inicio, y_inicio, x_fin, y_fin, color):
        dx = x_fin - x_inicio
        dy = y_fin - y_inicio
        pasos = max(abs(dx), abs(dy))
        if pasos == 0:
            self.dibujar_pixel(x_inicio, y_inicio, color)
            return
        x_incremental = dx / pasos
        y_incremental = dy / pasos
        x, y = x_inicio, y_inicio
        for _ in range(round(pasos) + 1):
            self.dibujar_pixel(x, y, color)
            x += x_incremental
            y += y_incremental

    def relleno_scanline(self, vertices, color):
        if not vertices or len(vertices) < 3:
            return
        y_min = math.ceil(min(v[1] for v in vertices))
        y_max = math.floor(max(v[1] for v in vertices))
        for y in range(y_min, y_max + 1):
            intersecciones = []
            for i in range(len(vertices)):
                p1 = vertices[i]
                p2 = vertices[(i + 1) % len(vertices)]
                if p1[1] != p2[1] and min(p1[1], p2[1]) <= y < max(p1[1], p2[1]):
                    x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                    intersecciones.append(x)
            intersecciones.sort()
            for i in range(0, len(intersecciones), 2):
                if i + 1 < len(intersecciones):
                    x_inicio = math.ceil(intersecciones[i])
                    x_fin = math.floor(intersecciones[i + 1])
                    for x in range(x_inicio, x_fin + 1):
                        self.dibujar_pixel(x, y, color)

    def relleno_inundacion(self, semilla_x, semilla_y, color_relleno):
        ancho, alto = self.ventana.get_size()
        semilla_x, semilla_y = round(semilla_x), round(semilla_y)

        if not (0 <= semilla_x < ancho and 0 <= semilla_y < alto):
            return

        color_objetivo = self.ventana.get_at((semilla_x, semilla_y))

        if color_objetivo == color_relleno:
            return

        cola = collections.deque([(semilla_x, semilla_y)])

        while cola:
            x, y = cola.popleft()
            if 0 <= x < ancho and 0 <= y < alto and self.ventana.get_at((x, y)) == color_objetivo:
                self.dibujar_pixel(x, y, color_relleno)
                cola.append((x + 1, y))
                cola.append((x - 1, y))
                cola.append((x, y + 1))
                cola.append((x, y - 1))

    def dibujar_triangulo(self, x_inicio, y_inicio, x_fin, y_fin, color):
        p1 = (x_inicio, y_inicio)
        p2 = (x_fin, y_fin)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        p3 = (p2[0] - dy, p2[1] + dx)
        vertices = [p1, p2, p3]

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(3):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 3][0],
                                       vertices[(i + 1) % 3][1], color)
            centro_x = (vertices[0][0] + vertices[1][0] + vertices[2][0]) / 3
            centro_y = (vertices[0][1] + vertices[1][1] + vertices[2][1]) / 3
            self.relleno_inundacion(centro_x, centro_y, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(3):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 3][0],
                                       vertices[(i + 1) % 3][1], color)

    def dibujar_cuadrado(self, x_inicio, y_inicio, x_fin, y_fin, color):
        p1 = (x_inicio, y_inicio)
        p2 = (x_fin, y_fin)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        p3 = (p2[0] - dy, p2[1] + dx)
        p4 = (p1[0] - dy, p1[1] + dx)
        vertices = [p1, p2, p3, p4]

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(4):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 4][0],
                                       vertices[(i + 1) % 4][1], color)
            centro_x = (p1[0] + p3[0]) / 2
            centro_y = (p1[1] + p3[1]) / 2
            self.relleno_inundacion(centro_x, centro_y, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(4):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 4][0],
                                       vertices[(i + 1) % 4][1], color)

    def dibujar_estrella(self, x_centro, y_centro, radio, color):
        vertices = []
        radio_exterior = radio
        radio_interior = radio / 2.5
        for i in range(10):
            angulo = math.radians(-90 + i * 36)
            r = radio_exterior if i % 2 == 0 else radio_interior
            x = x_centro + r * math.cos(angulo)
            y = y_centro - r * math.sin(angulo)
            vertices.append((x, y))

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(10):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 10][0],
                                       vertices[(i + 1) % 10][1], color)
            self.relleno_inundacion(x_centro, y_centro, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(10):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 10][0],
                                       vertices[(i + 1) % 10][1], color)

    def dibujar_pentagono(self, x_centro, y_centro, radio, color):
        vertices = []
        for i in range(5):
            angulo = math.radians(90 + i * 72)
            x = x_centro + radio * math.cos(angulo)
            y = y_centro - radio * math.sin(angulo)
            vertices.append((round(x), round(y)))

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(5):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 5][0],
                                       vertices[(i + 1) % 5][1], color)
            self.relleno_inundacion(x_centro, y_centro, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(5):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % 5][0],
                                       vertices[(i + 1) % 5][1], color)

    def dibujar_circulo(self, x_origen, y_origen, radio, lados, color):
        vertices = []
        for i in range(lados):
            angulo = 2 * math.pi * i / lados
            x = x_origen + radio * math.cos(angulo)
            y = y_origen - radio * math.sin(angulo)
            vertices.append((x, y))

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(lados):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % lados][0],
                                       vertices[(i + 1) % lados][1], color)
            self.relleno_inundacion(x_origen, y_origen, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(lados):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % lados][0],
                                       vertices[(i + 1) % lados][1], color)

    def dibujar_circulo_coordenadas_polares(self, x_origen, y_origen, radio, color):
        pasos = 360
        vertices = []
        for i in range(pasos):
            angulo = math.radians(i * (360 / pasos))
            x = x_origen + radio * math.cos(angulo)
            y = y_origen - radio * math.sin(angulo)
            vertices.append((x, y))

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(pasos):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % pasos][0],
                                       vertices[(i + 1) % pasos][1], color)
            self.relleno_inundacion(x_origen, y_origen, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(pasos):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % pasos][0],
                                       vertices[(i + 1) % pasos][1], color)

    def dibujar_elipse(self, x_origen, y_origen, x_vertice, y_vertice, longitud_menor, color):
        dx, dy = x_vertice - x_origen, y_vertice - y_origen
        a = math.sqrt(dx ** 2 + dy ** 2)
        theta = math.atan2(dy, dx)
        pasos = 100
        vertices = []
        for i in range(pasos):
            t = 2 * math.pi * i / pasos
            x_p = a * math.cos(t)
            y_p = longitud_menor * math.sin(t)
            x = x_origen + x_p * math.cos(theta) - y_p * math.sin(theta)
            y = y_origen + x_p * math.sin(theta) + y_p * math.cos(theta)
            vertices.append((x, y))

        if self.relleno_activo and self.metodo_relleno == 'inundacion':
            for i in range(pasos):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % pasos][0],
                                       vertices[(i + 1) % pasos][1], color)
            self.relleno_inundacion(x_origen, y_origen, self.color_relleno)
        else:
            if self.relleno_activo and self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            for i in range(pasos):
                self.dibujar_linea_dda(vertices[i][0], vertices[i][1], vertices[(i + 1) % pasos][0],
                                       vertices[(i + 1) % pasos][1], color)

    def dibujar_poligono(self, vertices, color):
        if self.relleno_activo:
            if self.metodo_relleno == 'scanline':
                self.relleno_scanline(vertices, self.color_relleno)
            elif self.metodo_relleno == 'inundacion':
                for i in range(len(vertices)):
                    p1 = vertices[i]
                    p2 = vertices[(i + 1) % len(vertices)]
                    self.dibujar_linea_dda(p1[0], p1[1], p2[0], p2[1], color)
                centro_x = sum(v[0] for v in vertices) / len(vertices)
                centro_y = sum(v[1] for v in vertices) / len(vertices)
                self.relleno_inundacion(centro_x, centro_y, self.color_relleno)

        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            self.dibujar_linea_dda(p1[0], p1[1], p2[0], p2[1], color)

    def curva(self, puntos, x, y, esc_x, esc_y, color):
        punt = []
        for i in range(puntos):
            X = (math.pi / (puntos - 1)) * i
            Y = math.sin(X)
            x_coor = x + X * esc_x
            y_coor = y - Y * esc_y
            punt.append((x_coor, y_coor))

        for j in range(len(punt) - 1):
            punto_actual = punt[j]
            punto_sig = punt[j + 1]
            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_sig[0], punto_sig[1], color)

    def humito(self, puntos, x, y, esc_x, esc_y, color):
        lista_puntos = []
        rango_y = 2 * math.pi
        for i in range(puntos):
            Y = (rango_y / puntos) * i
            X = Y * math.cos(4 * Y)
            x_coor = x + X * esc_x
            y_coor = y - Y * esc_y
            lista_puntos.append((x_coor, y_coor))

        for i in range(len(lista_puntos) - 1):
            punto_actual = lista_puntos[i]
            punto_siguiente = lista_puntos[i + 1]
            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_siguiente[0], punto_siguiente[1], color)

    def curva_parametricamente(self, puntos, x, y, esc, color):
        lista_puntos = []
        rango_t = 10.0
        for i in range(puntos + 1):
            t = (rango_t / puntos) * i
            x_matematica = t - 3 * math.sin(t)
            y_matematica = 4 - 3 * math.cos(t)

            x_coor = x + x_matematica * esc
            y_coor = y - y_matematica * esc

            lista_puntos.append((x_coor, y_coor))

        for i in range(len(lista_puntos) - 1):
            punto_actual = lista_puntos[i]
            punto_siguiente = lista_puntos[i + 1]
            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_siguiente[0], punto_siguiente[1], color)

    def infinito(self, puntos, x, y, radio, color):
        lista_puntos = []
        rango_t = 2 * math.pi
        for i in range(puntos + 1):
            t = (rango_t / puntos) * i
            denominador = 1 + (math.cos(t) ** 2)
            X = radio * math.sin(t) / denominador
            Y = radio * math.sin(t) * math.cos(t) / denominador
            x_coor = x + X
            y_coor = y - Y
            lista_puntos.append((x_coor, y_coor))
        for i in range(len(lista_puntos) - 1):
            punto_actual = lista_puntos[i]
            punto_siguiente = lista_puntos[i + 1]

            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_siguiente[0], punto_siguiente[1], color)

    def mandala1(self, puntos, x, y, escala, color):
        lista_puntos = []
        rango_t = 2 * math.pi
        for i in range(puntos + 1):
            t = (rango_t / puntos) * i
            X = math.cos(t) + (1 / 2) * math.cos(7 * t) + (1 / 3) * math.sin(17 * t)
            Y = math.sin(t) + (1 / 2) * math.sin(7 * t) + (1 / 3) * math.cos(17 * t)

            x_coor = x + X * escala
            y_coor = y - Y * escala
            lista_puntos.append((x_coor, y_coor))

        for i in range(len(lista_puntos) - 1):
            punto_actual = lista_puntos[i]
            punto_siguiente = lista_puntos[i + 1]
            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_siguiente[0], punto_siguiente[1], color)

    def mandala2(self, puntos, x, y, escala, color):
        lista_puntos = []
        rango_t = 14 * math.pi
        for i in range(puntos + 1):
            t = (rango_t / puntos) * i
            X = 17 * math.cos(t) + 7 * math.cos((17 / 7) * t)
            Y = 17 * math.sin(t) - 7 * math.sin((17 / 7) * t)
            x_coor = x + X * escala
            y_coor = y - Y * escala
            lista_puntos.append((x_coor, y_coor))

        for i in range(len(lista_puntos) - 1):
            punto_actual = lista_puntos[i]
            punto_siguiente = lista_puntos[i + 1]
            self.dibujar_linea_dda(punto_actual[0], punto_actual[1], punto_siguiente[0], punto_siguiente[1], color)

    def mallado(self, puntosX, puntosY, color):
        for y in puntosY:
            for i in range(len(puntosX) - 1):
                x1 = puntosX[i]
                x2 = puntosX[i + 1]
                self.dibujar_linea_dda(x1, y, x2, y, color)
        for x in puntosX:
            for j in range(len(puntosY) - 1):
                y1 = puntosY[j]
                y2 = puntosY[j + 1]
                self.dibujar_linea_dda(x, y1, x, y2, color)