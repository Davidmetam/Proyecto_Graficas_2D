import threading
import time

class Hilos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.pos_dx = 0.0
        self.pos_dy = 0.0
        self.angulo_actual = 0.0
        self.lock_trans = threading.Lock()
        self.lock_rotacion = threading.Lock()
        self.running = True
        self.hilo_animacion = None
        self.hilo_rotacion = None

    def iniciar_traslacion_lineal(self, x_final, y_final, pasos=200):
        self.destino_x = x_final
        self.destino_y = y_final
        self.pasos_totales = pasos

        if self.hilo_animacion is None or not self.hilo_animacion.is_alive():
            self.hilo_animacion = threading.Thread(target=self._ejecutar_traslacion, daemon=True)
            self.hilo_animacion.start()

    def _ejecutar_traslacion(self):
        incremento_x = self.destino_x / self.pasos_totales
        incremento_y = self.destino_y / self.pasos_totales
        for i in range(self.pasos_totales):
            if not self.running:
                break
            with self.lock_trans:
                self.pos_dx += incremento_x
                self.pos_dy += incremento_y
            time.sleep(0.01)
        with self.lock_trans:
            self.pos_dx = float(self.destino_x)
            self.pos_dy = float(self.destino_y)

    def iniciar_rotacion_continua(self, velocidad=1):
        self.velocidad_rotacion = velocidad
        if self.hilo_rotacion is None or not self.hilo_rotacion.is_alive():
            self.hilo_rotacion = threading.Thread(target=self._ejecutar_rotacion, daemon=True)
            self.hilo_rotacion.start()

    def _ejecutar_rotacion(self):
        while self.running:
            with self.lock_rotacion:
                self.angulo_actual = (self.angulo_actual + self.velocidad_rotacion) % 360
            time.sleep(0.01)

