#Ejercicio 8
'''Crea una clase "Tienda" con propiedades para el nombre de la
tienda y una lista de productos disponibles, y métodos para añadir
o eliminar productos de la lista y para obtener la lista completa de productos.'''

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append (producto)

    def eliminar_producto(self, producto):
        self.productos.remove (producto)
        
    def obtener_productos(self):
        return self.productos

# Ejemplo de uso de la clase Tienda
if __name__ == "__main__":
    tienda1 = Tienda ("Cuchara de Azúcar")
    
    tienda1.agregar_producto ("manzanas")
    tienda1.agregar_producto ("huevo")
    tienda1.agregar_producto ("azucar")
    tienda1.agregar_producto ("harina")
    tienda1.agregar_producto ("leche")
    tienda1.agregar_producto ("pan")

    print(f"Productos: {tienda1.obtener_productos()}")
    
    tienda1.eliminar_producto ("pan")
    tienda1.eliminar_producto ("azucar")
    print(f"Productos actualizados: {tienda1.obtener_productos()}")