class Asiento:
    def _init_ (self,color,precio,registro):
        self.color = str(color)
        self.precio = int(precio)
        self.registro = int(registro)
          
class Auto:
    cantidadCreados = 0
    def _init_ (self,modelo,precio,asiento,marca,motor,registro):
        modelo = str(modelo)
        precio = int(precio)
        asiento = []
        marca = str(marca)
        motor = motor
        registro = int(registro)

class Motor:
    def _init_ (self,numeroCilindros, tipo, registro):
        numeroCilindros = int(numeroCilindros)
        tipo = str(tipo)
        registro = int(registro)
