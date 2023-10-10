class ClaseA:
    def mensaje(self):
        print("Mensaje de Clase A")


class ClaseB:
    def mensaje(self):
        print("Mensaje de Clase B")


class ClaseC(ClaseA, ClaseB):
    def mensaje_b(self):
        ClaseB.mensaje(self)


mi_objeto = ClaseC()
#mi_objeto.mensaje()
mi_objeto.mensaje_b()
