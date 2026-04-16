#Ejercicio 2
'''Crea una clase "Coche" con propiedades para la marca,
el modelo y el año de fabricación, y un método para obtener
el número de años que ha pasado desde que se fabricó el coche.'''

class Coche:
    def __init__(self, marca, modelo, añoFabricacion):
        self.marca = marca
        self.modelo = modelo
        self.añoFabricacion = añoFabricacion

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_añoFabricacion(self):
        return self.añoFabricacion

    def establecer_añoFabricacion(self, añoFabricacion):
        self.añoFabricacion = añoFabricacion
        
    def calcular_antiguedad (self, añoActual):
        return añoActual - self.añoFabricacion

# Ejemplo de uso de la clase Coche
if __name__ == "__main__":
    coche1 = Coche("Lenovo", 205, 2012)

    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de Fabricación: {coche1.obtener_añoFabricacion()}")

    coche1.establecer_marca("Ford")
    coche1.establecer_modelo(207)
    coche1.establecer_añoFabricacion(2015)

    print("\nDespués de actualizar:")
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de Fabricación: {coche1.obtener_añoFabricacion()}")