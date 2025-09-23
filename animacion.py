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