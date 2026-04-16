#Ejercicio 7
'''Crea una clase "Banco" con propiedades para el nombre del
banco y la tasa de interés, y métodos para calcular el interés
que se obtendría en una cantidad determinada de dinero y el tiempo
que se tardaría en duplicar esa cantidad.'''

class Banco:
    def __init__(self, nombre, tasaInteres):
        self.nombre = nombre
        self.tasaInteres = tasaInteres

    def calcular_interes(self, plata):
        return plata * self.tasaInteres
    
    def tiempoEnDuplicar(self):
        return 72 / (self.tasaInteres * 100)
    
# Ejemplo de uso de la clase Banco
if __name__ == "__main__":
    banco1 = Banco ("Banco Universal", 0.23)
    
    interes = banco1.calcular_interes(1000)
    print(f"Interés generado: {interes}")
    
    tiempo = banco1.tiempoEnDuplicar()
    print(f"Tiempo que se tarda en duplicar: {tiempo} años")