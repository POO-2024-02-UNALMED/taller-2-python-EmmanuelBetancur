class Asiento:
    def __init__ (self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,ncolor):
        colores = ("rojo", "verde", "amarillo", "negro", "blanco")
        if ncolor in colores:
            self.color = ncolor
          
class Auto:
    cantidadCreados = 0
    def __init__ (self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for x in self.asientos:
                if x.registro == self.registro:
                    return "Auto original"
                else: return "Las piezas no son originales"
        else: return "Las piezas no son originales"

class Motor:
    def __init__ (self,numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nregistro):
        if type(nregistro) == int:
            self.registro = nregistro

    def asignarTipo(self, ntipo):
        if type(ntipo) == str:
            tipos = ("electrico", "gasolina")
            if ntipo in tipos:
                self.tipo = ntipo