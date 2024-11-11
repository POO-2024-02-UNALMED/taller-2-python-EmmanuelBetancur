class Asiento:
    def _init_ (self,color,precio,registro):
        self.color = str(color)
        self.precio = int(precio)
        self.registro = int(registro)

    def cambiarColor(self,ncolor):
        colores = ("rojo", "verde", "amarillo", "negro", "blanco")
        if ncolor in colores:
            self.color = ncolor
          
class Auto:
    cantidadCreados = 0
    def _init_ (self,modelo,precio,asientos,marca,motor,registro):
        modelo = str(modelo)
        precio = int(precio)
        asientos = []
        marca = str(marca)
        motor = motor
        registro = int(registro)
    
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
    def _init_ (self,numeroCilindros, tipo, registro):
        numeroCilindros = int(numeroCilindros)
        tipo = str(tipo)
        registro = int(registro)

    def cambiarRegistro(self, nregistro):
        if type(nregistro) == int:
            self.registro = nregistro

    def asignarTipo(self, ntipo):
        if type(ntipo) == str:
            tipos = ("electrico", "gasolina")
            if ntipo in tipos:
                self.tipo = ntipo