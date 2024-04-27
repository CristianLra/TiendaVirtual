class ModuloUsuario:
    def __init__(self,nombre,docIdentidad):
        self.nombre = nombre
        self.docIdentidad = docIdentidad

class Tienda:
    def __init__(self, nombreTienda= "SCB ACCESORIOS"):
        self.nombreTienda = nombreTienda

    def setNTienda(self, nombreTienda):
        self.nombreTienda = nombreTienda
    
    def getNTienda(self):
        return self.nombreTienda

    def AgregarProducto(self):
        self.setNTienda(input("Agrega tu producto: "))

objeto = Tienda()
print(objeto.nombreTienda)
objeto.AgregarProducto()
