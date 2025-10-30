import threading
import time


class Hilos3D:
    def __init__(self, ventana):
        self.ventana = ventana
        self.running = True

        self.tx = 0.0
        self.ty = 0.0
        self.tz = 0.0
        self.sx = 1.0
        self.sy = 1.0
        self.sz = 1.0
        self.angulo_x = 0.0
        self.angulo_y = 0.0
        self.angulo_z = 0.0

        self.lock_traslacion = threading.Lock()
        self.lock_escalado = threading.Lock()
        self.lock_rotacion_x = threading.Lock()
        self.lock_rotacion_y = threading.Lock()
        self.lock_rotacion_z = threading.Lock()

        self.hilo_traslacion = None
        self.hilo_escalado = None
        self.hilo_rotacion_x = None
        self.hilo_rotacion_y = None
        self.hilo_rotacion_z = None

    def iniciar_traslacion_3d(self, tx_final, ty_final, tz_final, pasos=100):
        self.destino_tx = tx_final
        self.destino_ty = ty_final
        self.destino_tz = tz_final
        self.pasos_totales_trans = pasos

        if self.hilo_traslacion is None or not self.hilo_traslacion.is_alive():
            self.hilo_traslacion = threading.Thread(target=self._ejecutar_traslacion_3d, daemon=True)
            self.hilo_traslacion.start()

    def _ejecutar_traslacion_3d(self):
        with self.lock_traslacion:
            self.tx = 0.0
            self.ty = 0.0
            self.tz = 0.0

        inc_x = self.destino_tx / self.pasos_totales_trans
        inc_y = self.destino_ty / self.pasos_totales_trans
        inc_z = self.destino_tz / self.pasos_totales_trans

        for _ in range(self.pasos_totales_trans):
            if not self.running:
                break
            with self.lock_traslacion:
                self.tx += inc_x
                self.ty += inc_y
                self.tz += inc_z
            time.sleep(0.01)

        with self.lock_traslacion:
            self.tx = float(self.destino_tx)
            self.ty = float(self.destino_ty)
            self.tz = float(self.destino_tz)

    def iniciar_escalado_3d(self, sx_final, sy_final, sz_final, pasos=100):
        self.destino_sx = sx_final
        self.destino_sy = sy_final
        self.destino_sz = sz_final
        self.pasos_totales_esc = pasos

        if self.hilo_escalado is None or not self.hilo_escalado.is_alive():
            self.hilo_escalado = threading.Thread(target=self._ejecutar_escalado_3d, daemon=True)
            self.hilo_escalado.start()

    def _ejecutar_escalado_3d(self):
        with self.lock_escalado:
            self.sx = 1.0
            self.sy = 1.0
            self.sz = 1.0

        inc_sx = (self.destino_sx - 1.0) / self.pasos_totales_esc
        inc_sy = (self.destino_sy - 1.0) / self.pasos_totales_esc
        inc_sz = (self.destino_sz - 1.0) / self.pasos_totales_esc

        for _ in range(self.pasos_totales_esc):
            if not self.running:
                break
            with self.lock_escalado:
                self.sx += inc_sx
                self.sy += inc_sy
                self.sz += inc_sz
            time.sleep(0.01)

        with self.lock_escalado:
            self.sx = float(self.destino_sx)
            self.sy = float(self.destino_sy)
            self.sz = float(self.destino_sz)

    def iniciar_rotacion_x_3d(self, angulo_final, pasos=100):
        self.destino_angulo_x = angulo_final
        self.pasos_totales_rot_x = pasos

        if self.hilo_rotacion_x is None or not self.hilo_rotacion_x.is_alive():
            self.hilo_rotacion_x = threading.Thread(target=self._ejecutar_rotacion_x_3d, daemon=True)
            self.hilo_rotacion_x.start()

    def _ejecutar_rotacion_x_3d(self):
        with self.lock_rotacion_x:
            self.angulo_x = 0.0

        inc_angulo_x = self.destino_angulo_x / self.pasos_totales_rot_x

        for _ in range(self.pasos_totales_rot_x):
            if not self.running:
                break
            with self.lock_rotacion_x:
                self.angulo_x += inc_angulo_x
            time.sleep(0.01)

        with self.lock_rotacion_x:
            self.angulo_x = float(self.destino_angulo_x)

    def iniciar_rotacion_y_3d(self, angulo_final, pasos=100):
        self.destino_angulo_y = angulo_final
        self.pasos_totales_rot_y = pasos

        if self.hilo_rotacion_y is None or not self.hilo_rotacion_y.is_alive():
            self.hilo_rotacion_y = threading.Thread(target=self._ejecutar_rotacion_y_3d, daemon=True)
            self.hilo_rotacion_y.start()

    def _ejecutar_rotacion_y_3d(self):
        with self.lock_rotacion_y:
            self.angulo_y = 0.0

        inc_angulo_y = self.destino_angulo_y / self.pasos_totales_rot_y

        for _ in range(self.pasos_totales_rot_y):
            if not self.running:
                break
            with self.lock_rotacion_y:
                self.angulo_y += inc_angulo_y
            time.sleep(0.01)

        with self.lock_rotacion_y:
            self.angulo_y = float(self.destino_angulo_y)

    def iniciar_rotacion_z_3d(self, angulo_final, pasos=100):
        self.destino_angulo_z = angulo_final
        self.pasos_totales_rot_z = pasos

        if self.hilo_rotacion_z is None or not self.hilo_rotacion_z.is_alive():
            self.hilo_rotacion_z = threading.Thread(target=self._ejecutar_rotacion_z_3d, daemon=True)
            self.hilo_rotacion_z.start()

    def _ejecutar_rotacion_z_3d(self):
        with self.lock_rotacion_z:
            self.angulo_z = 0.0

        inc_angulo_z = self.destino_angulo_z / self.pasos_totales_rot_z

        for _ in range(self.pasos_totales_rot_z):
            if not self.running:
                break
            with self.lock_rotacion_z:
                self.angulo_z += inc_angulo_z
            time.sleep(0.01)

        with self.lock_rotacion_z:
            self.angulo_z = float(self.destino_angulo_z)