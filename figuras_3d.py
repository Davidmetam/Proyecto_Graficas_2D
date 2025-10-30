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