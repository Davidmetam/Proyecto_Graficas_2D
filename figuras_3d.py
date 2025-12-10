import math
from figuras import Figuras


class Figuras3D(Figuras):


    def __init__(self, ventana):
        super().__init__(ventana)

    def _proyectar_y_dibujar_fugado(self, vertices_3d, aristas, punto_de_fuga, color):
        Xp, Yp, Zp = punto_de_fuga[0], punto_de_fuga[1], punto_de_fuga[2]
        if Zp == 0:
            return

        vertices_proyectados = []
        for v in vertices_3d:
            X1, Y1, Z1 = v[0], v[1], v[2]

            denominador = Zp - Z1
            if denominador == 0:
                denominador = 0.0001

            U = -Z1 / denominador
            X_proy = X1 + (Xp - X1) * U
            Y_proy = Y1 + (Yp - Y1) * U
            vertices_proyectados.append((X_proy, Y_proy))

        for arista_indices in aristas:
            p1_idx = arista_indices[0]
            p2_idx = arista_indices[1]
            v_inicio = vertices_proyectados[p1_idx]
            v_fin = vertices_proyectados[p2_idx]
            self.dibujar_linea_dda(v_inicio[0], v_inicio[1], v_fin[0], v_fin[1], color)

    def _proyectar_y_dibujar_proyectado(self, vertices_3d, aristas, punto_de_proyeccion, color):
        Xp, Yp, Zp = punto_de_proyeccion[0], punto_de_proyeccion[1], punto_de_proyeccion[2]
        if Zp == 0:
            return

        vertices_proyectados = []
        for v in vertices_3d:
            X1, Y1, Z1 = v[0], v[1], v[2]
            U = -Z1 / Zp
            X_proy = X1 + Xp * U
            Y_proy = Y1 + Yp * U
            vertices_proyectados.append((X_proy, Y_proy))

        for arista_indices in aristas:
            p1_idx = arista_indices[0]
            p2_idx = arista_indices[1]
            v_inicio = vertices_proyectados[p1_idx]
            v_fin = vertices_proyectados[p2_idx]
            self.dibujar_linea_dda(v_inicio[0], v_inicio[1], v_fin[0], v_fin[1], color)

    def crear_cubo(self, punto_inicial, arista):
        x, y, z = punto_inicial[0], punto_inicial[1], punto_inicial[2]

        v1 = (x, y, z)
        v2 = (x + arista, y, z)
        v3 = (x + arista, y + arista, z)
        v4 = (x, y + arista, z)

        v5 = (x, y, z + arista)
        v6 = (x + arista, y, z + arista)
        v7 = (x + arista, y + arista, z + arista)
        v8 = (x, y + arista, z + arista)

        return [v1, v2, v3, v4, v5, v6, v7, v8]

    def dibujar_cubo_proyectado(self, punto_inicial, arista, punto_de_proyeccion, color):
        vertices_3d = self.crear_cubo(punto_inicial, arista)
        aristas = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self._proyectar_y_dibujar_proyectado(vertices_3d, aristas, punto_de_proyeccion, color)

    def dibujar_cubo_fugado(self, punto_inicial, arista, punto_de_fuga, color):
        vertices_3d = self.crear_cubo(punto_inicial, arista)
        aristas = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self._proyectar_y_dibujar_fugado(vertices_3d, aristas, punto_de_fuga, color)

    def crear_piramide(self, punto_inicial, arista_base, altura):
        x, y, z = punto_inicial[0], punto_inicial[1], punto_inicial[2]
        v1 = (x, y, z)
        v2 = (x + arista_base, y, z)
        v3 = (x + arista_base, y, z + arista_base)
        v4 = (x, y, z + arista_base)
        x_centro = x + arista_base / 2
        y_apice = y - altura
        z_centro = z + arista_base / 2
        v5 = (x_centro, y_apice, z_centro)
        return [v1, v2, v3, v4, v5]

    def dibujar_piramide_proyectada(self, punto_inicial, arista_base, altura, punto_de_proyeccion, color):
        vertices_3d = self.crear_piramide(punto_inicial, arista_base, altura)
        aristas = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 4), (2, 4), (3, 4)
        ]
        self._proyectar_y_dibujar_proyectado(vertices_3d, aristas, punto_de_proyeccion, color)

    def dibujar_piramide_fugada(self, punto_inicial, arista_base, altura, punto_de_fuga, color):
        vertices_3d = self.crear_piramide(punto_inicial, arista_base, altura)
        aristas = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 4), (2, 4), (3, 4)
        ]
        self._proyectar_y_dibujar_fugado(vertices_3d, aristas, punto_de_fuga, color)

    def crear_reloj_arena(self, centro, escala, t_min, t_max, pasos_t, pasos_phi):
        vertices_3d = []
        aristas = []
        cx, cy, cz = centro
        t_rango = t_max - t_min

        for i in range(pasos_t + 1):
            t = t_min + (t_rango * i / pasos_t)

            radio = (2 - math.cos(t))

            vy = cy - (t * escala)
            for j in range(pasos_phi):
                phi = (2 * math.pi * j / pasos_phi)
                vx = cx + (radio * math.cos(phi) * escala)
                vz = cz + (radio * math.sin(phi) * escala)
                vertices_3d.append((vx, vy, vz))

        for i in range(pasos_t + 1):
            for j in range(pasos_phi):
                idx1 = i * pasos_phi + j
                idx2 = i * pasos_phi + (j + 1) % pasos_phi
                aristas.append((idx1, idx2))

        for j in range(pasos_phi):
            for i in range(pasos_t):
                idx1 = i * pasos_phi + j
                idx2 = (i + 1) * pasos_phi + j
                aristas.append((idx1, idx2))

        return vertices_3d, aristas

    def dibujar_reloj_arena_proyectado(self, centro, escala, t_min, t_max, pasos_t, pasos_phi, punto_de_proyeccion,
                                       color):
        vertices_3d, aristas = self.crear_reloj_arena(centro, escala, t_min, t_max, pasos_t, pasos_phi)
        self._proyectar_y_dibujar_proyectado(vertices_3d, aristas, punto_de_proyeccion, color)

    def dibujar_reloj_arena_fugado(self, centro, escala, t_min, t_max, pasos_t, pasos_phi, punto_de_fuga,
                                   color=(0, 0, 0)):
        vertices_3d, aristas = self.crear_reloj_arena(centro, escala, t_min, t_max, pasos_t, pasos_phi)
        self._proyectar_y_dibujar_fugado(vertices_3d, aristas, punto_de_fuga, color)

    def crear_reloj_arena_caras(self, centro, escala, t_min, t_max, pasos_t, pasos_phi):

        vertices_3d = []
        caras_con_datos = []
        cx, cy, cz = centro
        t_rango = t_max - t_min

        for i in range(pasos_t + 1):
            t = t_min + (t_rango * i / pasos_t)
            radio = (2 - math.cos(t))
            vy = cy - (t * escala)
            for j in range(pasos_phi):
                phi = (2 * math.pi * j / pasos_phi)
                vx = cx + (radio * math.cos(phi) * escala)
                vz = cz + (radio * math.sin(phi) * escala)
                vertices_3d.append((vx, vy, vz))

        for i in range(pasos_t):
            t = t_min + (t_rango * i / pasos_t)
            t_norm = (t - t_min) / t_rango

            if t_norm < 0.25:
                r = 0
                g = int(4 * 255 * t_norm)
                b = 255
            elif t_norm < 0.5:
                r = 0
                g = 255
                b = int(255 * (1 - 4 * (t_norm - 0.25)))
            elif t_norm < 0.75:
                r = int(255 * 4 * (t_norm - 0.5))
                g = 255
                b = 0
            else:
                r = 255
                g = int(255 * (1 - 4 * (t_norm - 0.75)))
                b = 0

            color = (r, g, b)

            for j in range(pasos_phi):
                idx1 = i * pasos_phi + j
                idx2 = i * pasos_phi + (j + 1) % pasos_phi
                idx3 = (i + 1) * pasos_phi + (j + 1) % pasos_phi
                idx4 = (i + 1) * pasos_phi + j

                vertices_cara = (idx1, idx2, idx3, idx4)

                z_promedio = (vertices_3d[idx1][2] + vertices_3d[idx2][2] +
                              vertices_3d[idx3][2] + vertices_3d[idx4][2]) / 4

                caras_con_datos.append((z_promedio, vertices_cara, color))

        return vertices_3d, caras_con_datos

    def _proyectar_y_dibujar_superficie(self, vertices_3d, caras_con_datos, punto_de_proyeccion, borde_color):
        Xp, Yp, Zp = punto_de_proyeccion[0], punto_de_proyeccion[1], punto_de_proyeccion[2]
        if Zp == 0:
            return

        vertices_proyectados = []
        for v in vertices_3d:
            X1, Y1, Z1 = v[0], v[1], v[2]
            U = -Z1 / Zp
            X_proy = X1 + Xp * U
            Y_proy = Y1 + Yp * U
            vertices_proyectados.append((X_proy, Y_proy))

        caras_actualizadas = []
        for _, vertices_indices, color_relleno in caras_con_datos:
            z_promedio_actualizado = (vertices_3d[vertices_indices[0]][2] +
                                      vertices_3d[vertices_indices[1]][2] +
                                      vertices_3d[vertices_indices[2]][2] +
                                      vertices_3d[vertices_indices[3]][2]) / 4
            caras_actualizadas.append((z_promedio_actualizado, vertices_indices, color_relleno))

        caras_actualizadas.sort(key=lambda x: x[0], reverse=True)

        for z, vertices_indices, color_relleno in caras_actualizadas:
            vertices_2d_cara = [
                vertices_proyectados[vertices_indices[0]],
                vertices_proyectados[vertices_indices[1]],
                vertices_proyectados[vertices_indices[2]],
                vertices_proyectados[vertices_indices[3]]
            ]

            self.relleno_scanline(vertices_2d_cara, color_relleno)

            if borde_color:
                for k in range(4):
                    p_inicio = vertices_2d_cara[k]
                    p_fin = vertices_2d_cara[(k + 1) % 4]
                    self.dibujar_linea_dda(p_inicio[0], p_inicio[1], p_fin[0], p_fin[1], color_relleno)

    def dibujar_reloj_arena_superficie_proyectado(self, centro, escala, t_min, t_max, pasos_t, pasos_phi,
                                                  punto_de_proyeccion, borde_color=None):
        vertices_3d, caras_con_datos = self.crear_reloj_arena_caras(centro, escala, t_min, t_max, pasos_t, pasos_phi)
        self._proyectar_y_dibujar_superficie(vertices_3d, caras_con_datos, punto_de_proyeccion, borde_color)


    def crear_esfera(self, centro, radio, pasos_theta, pasos_phi):
        vertices_3d = []
        aristas = []
        a, b, c = centro

        for i in range(pasos_theta + 1):
            theta = 2 * math.pi * i / pasos_theta
            for j in range(pasos_phi + 1):
                phi = math.pi * j / pasos_phi
                x = radio * math.cos(theta) * math.sin(phi) + a
                y = radio * math.sin(theta) * math.sin(phi) + b
                z = radio * math.cos(phi) + c
                vertices_3d.append((x, y, z))

        for i in range(pasos_theta + 1):
            for j in range(pasos_phi):
                idx1 = i * (pasos_phi + 1) + j
                idx2 = i * (pasos_phi + 1) + (j + 1)
                aristas.append((idx1, idx2))

        for i in range(pasos_theta):
            for j in range(pasos_phi + 1):
                idx1 = i * (pasos_phi + 1) + j
                idx2 = (i + 1) * (pasos_phi + 1) + j
                aristas.append((idx1, idx2))

        return vertices_3d, aristas

    def crear_esfera_caras(self, centro, radio, pasos_theta, pasos_phi):
        vertices_3d = []
        caras_con_datos = []
        a, b, c = centro

        color = (61, 138, 6)
        ROJO = (255, 0, 0)
        BLANCO = (255, 255, 255)
        GRIS = (192, 192, 192)

        for i in range(pasos_theta + 1):
            theta = 2 * math.pi * i / pasos_theta
            for j in range(pasos_phi + 1):
                phi = math.pi * j / pasos_phi

                z = radio * math.cos(theta) * math.sin(phi) + c
                y = radio * math.sin(theta) * math.sin(phi) + b
                x = radio * math.cos(phi) + a
                vertices_3d.append((x, y, z))

        for i in range(pasos_theta):
            for j in range(pasos_phi):
                idx1 = i * (pasos_phi + 1) + j
                idx2 = idx1 + 1
                idx3 = (i + 1) * (pasos_phi + 1) + j + 1
                idx4 = (i + 1) * (pasos_phi + 1) + j

                vertices_cara = (idx1, idx2, idx3, idx4)

                z_promedio = (
                                     vertices_3d[idx1][2] +
                                     vertices_3d[idx2][2] +
                                     vertices_3d[idx3][2] +
                                     vertices_3d[idx4][2]
                             ) / 4

                if (j // 5) % 2 == 0:
                    if i % 2 == 0:
                        color_cara = BLANCO
                    else:
                        color_cara = ROJO
                else:
                    color_cara = color

                caras_con_datos.append((z_promedio, vertices_cara, color_cara))

        start_idx_arillo = len(vertices_3d)
        polo_x = a + radio

        centro_arillo = (polo_x, b, c)
        radio_grande = 12
        radio_pequeno = 3
        pasos_u = 16
        pasos_v = 8

        for i in range(pasos_u + 1):
            u = 2 * math.pi * i / pasos_u
            cos_u = math.cos(u)
            sin_u = math.sin(u)
            for j in range(pasos_v + 1):
                v = 2 * math.pi * j / pasos_v
                cos_v = math.cos(v)
                sin_v = math.sin(v)

                p_x = (radio_grande + radio_pequeno * cos_v)

                x_arillo = centro_arillo[0] + p_x * cos_u
                y_arillo = centro_arillo[1] + p_x * sin_u
                z_arillo = centro_arillo[2] + radio_pequeno * sin_v

                vertices_3d.append((x_arillo, y_arillo, z_arillo))

        for i in range(pasos_u):
            for j in range(pasos_v):
                idx1 = start_idx_arillo + i * (pasos_v + 1) + j
                idx2 = start_idx_arillo + i * (pasos_v + 1) + (j + 1)
                idx3 = start_idx_arillo + (i + 1) * (pasos_v + 1) + (j + 1)
                idx4 = start_idx_arillo + (i + 1) * (pasos_v + 1) + j

                vertices_cara_arillo = (idx1, idx2, idx3, idx4)

                z_promedio_arillo = (
                                            vertices_3d[idx1][2] +
                                            vertices_3d[idx2][2] +
                                            vertices_3d[idx3][2] +
                                            vertices_3d[idx4][2]
                                    ) / 4

                caras_con_datos.append((z_promedio_arillo, vertices_cara_arillo, GRIS))

        return vertices_3d, caras_con_datos

    def dibujar_esfera_proyectada(self, centro, radio, pasos_theta, pasos_phi, punto_de_proyeccion,
                                       color):
        vertices_3d, aristas = self.crear_esfera(centro, radio, pasos_theta, pasos_phi)
        self._proyectar_y_dibujar_proyectado(vertices_3d, aristas, punto_de_proyeccion, color)

    def crear_estrella_3d(self, centro, escala):
        cx, cy, cz = centro
        R = escala
        r = escala * 0.45

        vertices2d = []

        for i in range(5):
            ang_p = math.radians(i * 72 - 90)
            x = cx + R * math.cos(ang_p)
            y = cy + R * math.sin(ang_p)
            vertices2d.append((x, y, cz))

            ang_i = math.radians(i * 72 - 90 + 36)
            x = cx + r * math.cos(ang_i)
            y = cy + r * math.sin(ang_i)
            vertices2d.append((x, y, cz))

        centro_frente = (cx, cy, cz - escala * 0.3)
        centro_atras = (cx, cy, cz + escala * 0.3)

        vertices = vertices2d + [centro_frente, centro_atras]

        caras = []

        for i in range(10):
            i_next = (i + 1) % 10
            caras.append((10, i, i_next))

        for i in range(10):
            i_next = (i + 1) % 10
            caras.append((11, i_next, i))

        return vertices, caras


    def dibujar_estrella_3d_proyectada(self, vertices, caras, punto_de_proyeccion, color_relleno, color_borde):
        Xp, Yp, Zp = punto_de_proyeccion
        if Zp == 0:
            Zp = 0.001

        v2d = []
        for x, y, z in vertices:
            U = -z / Zp
            xp = x + Xp * U
            yp = y + Yp * U
            v2d.append((xp, yp))

        orden = []
        for a, b, c in caras:
            zprom = (vertices[a][2] + vertices[b][2] + vertices[c][2]) / 3
            orden.append((zprom, (a, b, c)))

        orden.sort(reverse=True)

        for _, (a, b, c) in orden:
            pts = [v2d[a], v2d[b], v2d[c]]
            self.relleno_scanline(pts, color_relleno)
            self.dibujar_linea_dda(pts[0][0], pts[0][1], pts[1][0], pts[1][1], color_borde)
            self.dibujar_linea_dda(pts[1][0], pts[1][1], pts[2][0], pts[2][1], color_borde)
            self.dibujar_linea_dda(pts[2][0], pts[2][1], pts[0][0], pts[0][1], color_borde)


    def dibujar_estrella_3d_superficie(self, centro, escala, punto_de_proyeccion):
        vertices, caras = self.crear_estrella_3d(centro, escala)
        color_relleno = (255, 255, 0)
        color_borde = (245, 187, 39)
        self.dibujar_estrella_3d_proyectada(vertices, caras, punto_de_proyeccion, color_relleno, color_borde)

    # Agregar estos métodos a la clase Figuras3D en figuras_3d.py

    def aplicar_sombreado_phong(self, color_base, normal, luz_pos, camara_pos, ka=0.2, kd=0.6, ks=0.4, shininess=32):
        """
        Aplica sombreado Phong para iluminación realista

        Args:
            color_base: Color RGB base de la superficie
            normal: Vector normal de la superficie (nx, ny, nz)
            luz_pos: Posición de la luz (x, y, z)
            camara_pos: Posición de la cámara (x, y, z)
            ka: Coeficiente ambiental
            kd: Coeficiente difuso
            ks: Coeficiente especular
            shininess: Brillo especular
        """
        # Normalizar el vector normal
        mag_n = math.sqrt(normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2)
        if mag_n == 0:
            return color_base
        n = (normal[0] / mag_n, normal[1] / mag_n, normal[2] / mag_n)

        # Componente ambiental
        r_amb = int(color_base[0] * ka)
        g_amb = int(color_base[1] * ka)
        b_amb = int(color_base[2] * ka)

        # Vector de luz (simplificado, asumiendo punto en origen)
        luz = (luz_pos[0], luz_pos[1], luz_pos[2])
        mag_l = math.sqrt(luz[0] ** 2 + luz[1] ** 2 + luz[2] ** 2)
        if mag_l == 0:
            return (r_amb, g_amb, b_amb)
        l = (luz[0] / mag_l, luz[1] / mag_l, luz[2] / mag_l)

        # Componente difusa (Lambert)
        dot_nl = max(0, n[0] * l[0] + n[1] * l[1] + n[2] * l[2])
        r_dif = int(color_base[0] * kd * dot_nl)
        g_dif = int(color_base[1] * kd * dot_nl)
        b_dif = int(color_base[2] * kd * dot_nl)

        # Vector de visión
        v = (camara_pos[0], camara_pos[1], camara_pos[2])
        mag_v = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        if mag_v > 0:
            v = (v[0] / mag_v, v[1] / mag_v, v[2] / mag_v)

            # Vector de reflexión: r = 2(n·l)n - l
            dot_nl_2 = 2 * dot_nl
            r = (dot_nl_2 * n[0] - l[0], dot_nl_2 * n[1] - l[1], dot_nl_2 * n[2] - l[2])

            # Componente especular
            dot_rv = max(0, r[0] * v[0] + r[1] * v[1] + r[2] * v[2])
            spec = dot_rv ** shininess
            r_spec = int(255 * ks * spec)
            g_spec = int(255 * ks * spec)
            b_spec = int(255 * ks * spec)
        else:
            r_spec = g_spec = b_spec = 0

        # Combinar componentes
        r_final = min(255, r_amb + r_dif + r_spec)
        g_final = min(255, g_amb + g_dif + g_spec)
        b_final = min(255, b_amb + b_dif + b_spec)

        return (r_final, g_final, b_final)

    def generar_textura_navideña_esfera(self, i, j, pasos_theta, pasos_phi, tiempo=0):
        """
        Genera patrones navideños para la esfera (rayas candy cane, cuadros)

        Args:
            i, j: Índices de la cara
            pasos_theta, pasos_phi: Resolución de la esfera
            tiempo: Para animación (opcional)
        """
        # Patrón de rayas diagonales estilo bastón de caramelo
        patron = (i + j + int(tiempo * 10)) % 8

        if patron < 4:
            # Rojo navideño
            return (200, 30, 30)
        else:
            # Blanco
            return (255, 255, 255)

    def generar_textura_estrella_brillante(self, distancia_centro, tiempo=0):
        """
        Genera efecto de brillo dorado para estrellas

        Args:
            distancia_centro: Distancia al centro de la estrella (0-1)
            tiempo: Para pulsación animada
        """
        # Efecto de brillo que pulsa
        pulsacion = 0.5 + 0.5 * math.sin(tiempo * 3)

        # Amarillo/dorado brillante en el centro, más oscuro en bordes
        brillo = (1 - distancia_centro) * pulsacion

        r = int(255 * (0.8 + 0.2 * brillo))
        g = int(220 * (0.7 + 0.3 * brillo))
        b = int(50 * brillo)

        return (min(255, r), min(255, g), min(255, b))

    def calcular_normal_cara(self, vertices_3d, indices_cara):
        """
        Calcula el vector normal de una cara usando producto cruz

        Args:
            vertices_3d: Lista de vértices 3D
            indices_cara: Tupla con índices de los vértices de la cara
        """
        # Tomar los primeros 3 vértices para calcular la normal
        v0 = vertices_3d[indices_cara[0]]
        v1 = vertices_3d[indices_cara[1]]
        v2 = vertices_3d[indices_cara[2]]

        # Vectores de los lados
        u = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
        v = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])

        # Producto cruz: u × v
        nx = u[1] * v[2] - u[2] * v[1]
        ny = u[2] * v[0] - u[0] * v[2]
        nz = u[0] * v[1] - u[1] * v[0]

        return (nx, ny, nz)

    def _proyectar_y_dibujar_superficie_con_iluminacion(self, vertices_3d, caras_con_datos,
                                                        punto_de_proyeccion, luz_pos,
                                                        usar_textura=False, tiempo=0):
        """
        Dibuja superficies con iluminación Phong y texturas opcionales

        Args:
            vertices_3d: Lista de vértices 3D
            caras_con_datos: Lista de tuplas (z, indices, color_base)
            punto_de_proyeccion: Punto de proyección
            luz_pos: Posición de la luz
            usar_textura: Si aplicar textura navideña
            tiempo: Para animaciones
        """
        Xp, Yp, Zp = punto_de_proyeccion[0], punto_de_proyeccion[1], punto_de_proyeccion[2]
        if Zp == 0:
            return

        vertices_proyectados = []
        for v in vertices_3d:
            X1, Y1, Z1 = v[0], v[1], v[2]
            U = -Z1 / Zp
            X_proy = X1 + Xp * U
            Y_proy = Y1 + Yp * U
            vertices_proyectados.append((X_proy, Y_proy))

        # Actualizar profundidades
        caras_actualizadas = []
        for _, vertices_indices, color_base in caras_con_datos:
            z_promedio = sum(vertices_3d[idx][2] for idx in vertices_indices) / len(vertices_indices)
            caras_actualizadas.append((z_promedio, vertices_indices, color_base))

        caras_actualizadas.sort(key=lambda x: x[0], reverse=True)

        for z, vertices_indices, color_base in caras_actualizadas:
            # Calcular normal de la cara
            normal = self.calcular_normal_cara(vertices_3d, vertices_indices)

            # Calcular centro de la cara para iluminación
            centro_cara = (
                sum(vertices_3d[idx][0] for idx in vertices_indices) / len(vertices_indices),
                sum(vertices_3d[idx][1] for idx in vertices_indices) / len(vertices_indices),
                sum(vertices_3d[idx][2] for idx in vertices_indices) / len(vertices_indices)
            )

            # Aplicar sombreado Phong
            color_iluminado = self.aplicar_sombreado_phong(
                color_base,
                normal,
                (luz_pos[0] - centro_cara[0], luz_pos[1] - centro_cara[1], luz_pos[2] - centro_cara[2]),
                punto_de_proyeccion,
                ka=0.3, kd=0.5, ks=0.6, shininess=64
            )

            # Proyectar vértices de la cara
            vertices_2d_cara = [vertices_proyectados[idx] for idx in vertices_indices]

            # Dibujar con el color iluminado
            self.relleno_scanline(vertices_2d_cara, color_iluminado)

            # Opcional: dibujar bordes sutiles
            for k in range(len(vertices_2d_cara)):
                p_inicio = vertices_2d_cara[k]
                p_fin = vertices_2d_cara[(k + 1) % len(vertices_2d_cara)]
                # Borde ligeramente más oscuro
                color_borde = (
                    max(0, color_iluminado[0] - 30),
                    max(0, color_iluminado[1] - 30),
                    max(0, color_iluminado[2] - 30)
                )
                self.dibujar_linea_dda(p_inicio[0], p_inicio[1], p_fin[0], p_fin[1], color_borde)

    def crear_esfera_caras_navideña(self, centro, radio, pasos_theta, pasos_phi, tiempo=0):
        """
        Crea esfera con textura navideña (rayas candy cane y adornos)
        """
        vertices_3d = []
        caras_con_datos = []
        a, b, c = centro

        ROJO_NAVIDAD = (200, 30, 30)
        BLANCO = (255, 255, 255)
        VERDE_NAVIDAD = (34, 139, 34)
        DORADO = (255, 215, 0)

        for i in range(pasos_theta + 1):
            theta = 2 * math.pi * i / pasos_theta
            for j in range(pasos_phi + 1):
                phi = math.pi * j / pasos_phi
                z = radio * math.cos(theta) * math.sin(phi) + c
                y = radio * math.sin(theta) * math.sin(phi) + b
                x = radio * math.cos(phi) + a
                vertices_3d.append((x, y, z))

        for i in range(pasos_theta):
            for j in range(pasos_phi):
                idx1 = i * (pasos_phi + 1) + j
                idx2 = idx1 + 1
                idx3 = (i + 1) * (pasos_phi + 1) + j + 1
                idx4 = (i + 1) * (pasos_phi + 1) + j

                vertices_cara = (idx1, idx2, idx3, idx4)
                z_promedio = sum(vertices_3d[idx][2] for idx in vertices_cara) / 4

                # Patrón de rayas diagonales navideñas
                patron = (i + j) % 6

                if patron < 2:
                    color_cara = ROJO_NAVIDAD
                elif patron < 4:
                    color_cara = BLANCO
                else:
                    color_cara = VERDE_NAVIDAD

                # Agregar algunos "adornos" dorados aleatorios
                if (i * 7 + j * 11) % 23 == 0:
                    color_cara = DORADO

                caras_con_datos.append((z_promedio, vertices_cara, color_cara))

        # Agregar el anillo (aro) como antes
        start_idx_arillo = len(vertices_3d)
        polo_x = a + radio
        centro_arillo = (polo_x, b, c)
        radio_grande = 12
        radio_pequeno = 3
        pasos_u = 16
        pasos_v = 8

        for i in range(pasos_u + 1):
            u = 2 * math.pi * i / pasos_u
            for j in range(pasos_v + 1):
                v = 2 * math.pi * j / pasos_v
                p_x = (radio_grande + radio_pequeno * math.cos(v))
                x_arillo = centro_arillo[0] + p_x * math.cos(u)
                y_arillo = centro_arillo[1] + p_x * math.sin(u)
                z_arillo = centro_arillo[2] + radio_pequeno * math.sin(v)
                vertices_3d.append((x_arillo, y_arillo, z_arillo))

        GRIS_METALICO = (192, 192, 192)
        for i in range(pasos_u):
            for j in range(pasos_v):
                idx1 = start_idx_arillo + i * (pasos_v + 1) + j
                idx2 = start_idx_arillo + i * (pasos_v + 1) + (j + 1)
                idx3 = start_idx_arillo + (i + 1) * (pasos_v + 1) + (j + 1)
                idx4 = start_idx_arillo + (i + 1) * (pasos_v + 1) + j
                vertices_cara_arillo = (idx1, idx2, idx3, idx4)
                z_promedio_arillo = sum(vertices_3d[idx][2] for idx in vertices_cara_arillo) / 4
                caras_con_datos.append((z_promedio_arillo, vertices_cara_arillo, GRIS_METALICO))

        return vertices_3d, caras_con_datos

    def dibujar_estrella_3d_con_brillo(self, vertices, caras, punto_de_proyeccion,
                                       luz_pos, tiempo=0):
        """
        Dibuja estrella con efecto de brillo dorado y sombreado
        """
        Xp, Yp, Zp = punto_de_proyeccion
        if Zp == 0:
            Zp = 0.001

        v2d = []
        for x, y, z in vertices:
            U = -z / Zp
            xp = x + Xp * U
            yp = y + Yp * U
            v2d.append((xp, yp))

        orden = []
        for a, b, c in caras:
            zprom = (vertices[a][2] + vertices[b][2] + vertices[c][2]) / 3
            orden.append((zprom, (a, b, c)))

        orden.sort(reverse=True)

        # Calcular centro de la estrella
        centro_x = sum(v[0] for v in vertices) / len(vertices)
        centro_y = sum(v[1] for v in vertices) / len(vertices)
        centro_z = sum(v[2] for v in vertices) / len(vertices)

        for _, (a, b, c_idx) in orden:
            pts = [v2d[a], v2d[b], v2d[c_idx]]

            # Calcular normal
            v_a = vertices[a]
            v_b = vertices[b]
            v_c = vertices[c_idx]
            normal = self.calcular_normal_cara(vertices, (a, b, c_idx))

            # Centro de la cara
            centro_cara = (
                (v_a[0] + v_b[0] + v_c[0]) / 3,
                (v_a[1] + v_b[1] + v_c[1]) / 3,
                (v_a[2] + v_b[2] + v_c[2]) / 3
            )

            # Color base dorado brillante
            COLOR_BASE_ESTRELLA = (255, 223, 0)

            # Aplicar sombreado
            color_iluminado = self.aplicar_sombreado_phong(
                COLOR_BASE_ESTRELLA,
                normal,
                (luz_pos[0] - centro_cara[0], luz_pos[1] - centro_cara[1], luz_pos[2] - centro_cara[2]),
                punto_de_proyeccion,
                ka=0.4, kd=0.4, ks=0.8, shininess=128  # Muy brillante
            )

            # Agregar pulsación
            pulsacion = 0.9 + 0.1 * math.sin(tiempo * 4)
            color_final = (
                int(color_iluminado[0] * pulsacion),
                int(color_iluminado[1] * pulsacion),
                int(color_iluminado[2] * 0.8 * pulsacion)  # Menos azul
            )

            self.relleno_scanline(pts, color_final)

            # Borde dorado más oscuro
            color_borde = (245, 187, 39)
            self.dibujar_linea_dda(pts[0][0], pts[0][1], pts[1][0], pts[1][1], color_borde)
            self.dibujar_linea_dda(pts[1][0], pts[1][1], pts[2][0], pts[2][1], color_borde)
            self.dibujar_linea_dda(pts[2][0], pts[2][1], pts[0][0], pts[0][1], color_borde)