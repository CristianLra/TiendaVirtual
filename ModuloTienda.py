class Tienda:
    def __init__(self, nombreTienda = "SCB ACCESORIOS"):
        self.nombreTienda = nombreTienda

    def setNombreTienda(self, nombreTienda):
        self.nombreTienda = nombreTienda
    
    def getNombreTienda(self):
        return self.nombreTienda

    def AgregarProducto(self):
        self.setNombreTienda(input("Agrega tu producto: "))
    
    def ListarProducto(self):
        inventario = [{
            'Nombre': 'Fundas para acientos',
            'Cantidad': 40,
            'Precio': 250.000,
        },
        {
            'Nombre': 'Organizadores para el interior',
            'Cantidad': 30,
            'Precio': 90.000,
        },
        {
            'Nombre': 'Cargadores de celular para vehiculos',
            'Cantidad': 50,
            'Precio': 50.000,
        },
        {
            'Nombre': 'Luces led para el interior o exterior',
            'Cantidad': 70,
            'Precio': 90.000,
        },
        {
            'Nombre': 'Kit de limpieza',
            'Cantidad': 40,
            'Precio': 140.000,
        },
        {
            'Nombre': 'Herramientas para mantenimiento',
            'Cantidad': 25,
            'Precio': 400.000,
        },
        {
            'Nombre': 'Accesorios personalizados (Emblemas o Pegatinas)',
            'Cantidad': 40,
            'Precio': 20.000,
        }]

        for articulos in inventario:
            for art in articulos.values():
                print(art)
                
    def EliminarProductos(self):
        pass
        
objeto = Tienda()
print(objeto.nombreTienda)
objeto.AgregarProducto()
objeto.ListarProducto()
