import math


class Animacion:
    def __init__(self, ventana):
        self.ventana = ventana

    def traslacion(self, figura, dx, dy):
        T = [[1, 0, dx], [0, 1, dy], [0, 0, 1]]
        res = []
        for x, y in figura:
            x_t = T[0][0] * x + T[0][1] * y + T[0][2] * 1
            y_t = T[1][0] * x + T[1][1] * y + T[1][2] * 1
            res.append((int(x_t), int(y_t)))
        return res

    def escalar(self, figura, sx, sy):
        T = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
        res = []
        for x, y in figura:
            x_t = T[0][0] * x + T[0][1] * y + T[0][2] * 1
            y_t = T[1][0] * x + T[1][1] * y + T[1][2] * 1
            res.append((int(x_t), int(y_t)))
        return res

    def rotar(self, figura, angulo, cx, cy):
        angulo_rad = math.radians(angulo)
        cos_a = math.cos(angulo_rad)
        sin_a = math.sin(angulo_rad)
        res = []
        for x, y in figura:
            x_temp = x - cx
            y_temp = y - cy
            x_rot = x_temp * cos_a - y_temp * sin_a
            y_rot = x_temp * sin_a + y_temp * cos_a
            x_final = x_rot + cx
            y_final = y_rot + cy
            res.append((int(x_final), int(y_final)))
        return res

    def traslacion_3d(self, vertices_3d, tx, ty, tz):
        vertices_transformados = []
        for x, y, z in vertices_3d:
            x_nuevo = x + tx
            y_nuevo = y + ty
            z_nuevo = z + tz
            vertices_transformados.append((x_nuevo, y_nuevo, z_nuevo))
        return vertices_transformados

    def escalar_3d(self, vertices_3d, sx, sy, sz, centro_x, centro_y, centro_z):
        vertices_transformados = []
        for x, y, z in vertices_3d:
            x_temp = x - centro_x
            y_temp = y - centro_y
            z_temp = z - centro_z

            x_esc = x_temp * sx
            y_esc = y_temp * sy
            z_esc = z_temp * sz

            x_nuevo = x_esc + centro_x
            y_nuevo = y_esc + centro_y
            z_nuevo = z_esc + centro_z
            vertices_transformados.append((x_nuevo, y_nuevo, z_nuevo))
        return vertices_transformados

    def rotacion_x_3d(self, vertices_3d, angulo, centro_x, centro_y, centro_z):
        angulo_rad = math.radians(angulo)
        cos_a = math.cos(angulo_rad)
        sin_a = math.sin(angulo_rad)
        vertices_transformados = []
        for x, y, z in vertices_3d:
            x_temp = x - centro_x
            y_temp = y - centro_y
            z_temp = z - centro_z

            x_rot = x_temp
            y_rot = y_temp * cos_a - z_temp * sin_a
            z_rot = y_temp * sin_a + z_temp * cos_a

            x_nuevo = x_rot + centro_x
            y_nuevo = y_rot + centro_y
            z_nuevo = z_rot + centro_z
            vertices_transformados.append((x_nuevo, y_nuevo, z_nuevo))
        return vertices_transformados

    def rotacion_y_3d(self, vertices_3d, angulo, centro_x, centro_y, centro_z):
        angulo_rad = math.radians(angulo)
        cos_a = math.cos(angulo_rad)
        sin_a = math.sin(angulo_rad)
        vertices_transformados = []
        for x, y, z in vertices_3d:
            x_temp = x - centro_x
            y_temp = y - centro_y
            z_temp = z - centro_z

            x_rot = x_temp * cos_a + z_temp * sin_a
            y_rot = y_temp
            z_rot = -x_temp * sin_a + z_temp * cos_a

            x_nuevo = x_rot + centro_x
            y_nuevo = y_rot + centro_y
            z_nuevo = z_rot + centro_z
            vertices_transformados.append((x_nuevo, y_nuevo, z_nuevo))
        return vertices_transformados

    def rotacion_z_3d(self, vertices_3d, angulo, centro_x, centro_y, centro_z):
        angulo_rad = math.radians(angulo)
        cos_a = math.cos(angulo_rad)
        sin_a = math.sin(angulo_rad)
        vertices_transformados = []
        for x, y, z in vertices_3d:
            x_temp = x - centro_x
            y_temp = y - centro_y
            z_temp = z - centro_z

            x_rot = x_temp * cos_a - y_temp * sin_a
            y_rot = x_temp * sin_a + y_temp * cos_a
            z_rot = z_temp

            x_nuevo = x_rot + centro_x
            y_nuevo = y_rot + centro_y
            z_nuevo = z_rot + centro_z
            vertices_transformados.append((x_nuevo, y_nuevo, z_nuevo))
        return vertices_transformados