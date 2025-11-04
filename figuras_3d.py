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
        import math

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
                    self.dibujar_linea_dda(p_inicio[0], p_inicio[1], p_fin[0], p_fin[1], borde_color)

    def dibujar_reloj_arena_superficie_proyectado(self, centro, escala, t_min, t_max, pasos_t, pasos_phi,
                                                  punto_de_proyeccion, borde_color=None):
        vertices_3d, caras_con_datos = self.crear_reloj_arena_caras(centro, escala, t_min, t_max, pasos_t, pasos_phi)
        self._proyectar_y_dibujar_superficie(vertices_3d, caras_con_datos, punto_de_proyeccion, borde_color)