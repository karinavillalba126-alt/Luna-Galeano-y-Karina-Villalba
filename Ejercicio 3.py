#Ejercicio 3
'''Crea una clase "Producto" con propiedades para el nombre,
el precio y el stock disponible, y métodos para aumentar o disminuir el stock.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_stock(self):
        return self.stock

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else: print ("No hay suficiente stock")

# Ejemplo de uso de la clase Producto
if __name__ == "__main__":
    producto1 = Producto("Ravioles", 1200, 5)

    print(f"Nombre del Producto: {producto1.nombre}")
    print(f"Precio: $ {producto1.precio}")
    print(f"Stock Disponible: {producto1.stock}")
    
    producto1.aumentar_stock(10)
    print(f"Stock después de aumentar: {producto1.stock}")
    
    producto1.aumentar_stock(2)
    print(f"Después de dismimuir: {producto1.stock}")
    