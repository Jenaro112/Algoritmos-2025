"""
Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, destino, kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados por clase (primera y turista). Implemente las funciones necesarias que permitan realizar las siguiente actividades:
-   a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
-   b. mostrar los vuelos con asientos clase turista disponible;
-   c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y primera clase ($203 por kilómetro);
-   d. mostrar los vuelos programados para una determinada fecha;
-   e. vender un asiento (o pasaje) para un determinado vuelo;
-   f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad de dinero a devovler;
-   g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
"""

from list_ import List

class Vuelo:
    def __init__(self, empresa, numero_vuelo, asientos_totales, fecha_salida, destino, kms, asientos_ocupados_turista=0, asientos_ocupados_primera=0):
        self.empresa = empresa
        self.numero_vuelo = numero_vuelo
        self.asientos_totales = asientos_totales
        self.fecha_salida = fecha_salida
        self.destino = destino
        self.kms = kms
        self.asientos_ocupados_turista = asientos_ocupados_turista
        self.asientos_ocupados_primera = asientos_ocupados_primera

    def __str__(self):
        return f"{self.numero_vuelo} - {self.empresa} ({self.destino}, {self.fecha_salida})"
    
    def Punto_A(self):
        return self.destino in ["Atenas", "Miconos", "Rodas"]
    
    def Punto_B(self):
        return self.asientos_totales - (self.asientos_ocupados_turista + self.asientos_ocupados_primera) > 0
    
    def Punto_C(self):
        recaudacion_turista = (self.asientos_totales - self.asientos_ocupados_turista - self.asientos_ocupados_primera) * 75 * self.kms
        recaudacion_primera = self.asientos_ocupados_primera * 203 * self.kms
        return recaudacion_turista + recaudacion_primera
    
    def Punto_D(self, fecha):
        return self.fecha_salida == fecha
    
    def Punto_E(self):
        if self.asientos_totales - (self.asientos_ocupados_turista + self.asientos_ocupados_primera) > 0:
            self.asientos_ocupados_turista += 1
            return True
        return False
    
    def Punto_F(self):
        if self.asientos_ocupados_turista + self.asientos_ocupados_primera > 0:
            dinero_a_devolver = (self.asientos_ocupados_turista * 75 * self.kms) + (self.asientos_ocupados_primera * 203 * self.kms)
            return dinero_a_devolver
        return 0
    
    def Punto_G(self):
        return self.destino == "Tailandia"
    
