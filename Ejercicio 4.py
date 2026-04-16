#Ejercicio 4
'''Crea una clase "Rectángulo" con propiedades para la longitud
y la anchura, y métodos para calcular el área y el perímetro del rectángulo.'''

class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def calcular_area(self):
        return self.longitud * self.anchura
    
    def calcular_perimetro(self):
        return 2* (self.longitud + self.anchura)
    
# Ejemplo de uso de la clase Rectángulo
if __name__ == "__main__":
    rectangulo1 = Rectangulo(6, 9)

    print(f"Área: {rectangulo1.calcular_area}")
    print(f"Perímetro: {rectangulo1.calcular_perimetro}")