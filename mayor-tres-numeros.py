"""
Determina el mayor de tres números ingresados por el teclado
"""

class OrdenarTresNumeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def intercambiar_valores(self, numero1, numero2):

        print(f"\nIntercambiando {numero1} y {numero2} ... \n")
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1, numero2

    def ingreser_numeros(self):
        print("\nIngrese los numeros ...")

        self.numero1=int(input("Ingresa el primer numero : "))
        self.numero2=int(input("Ingresa el segundo numero: "))
        self.numero3=int(input("Ingresa el tercer numero : "))

    def ordenar_numeros(self):

        print("\nOrdenando ...")
        if self.numero1 > self.numero2:
            self. numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

        if self.numero2 > self.numero3:
            self.numero2, self.numero3 = self.intercambiar_valores(self.numero2, self.numero3)

        if self.numero1 > self.numero2:
           self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

    def imprimir (self):
        print("\nImprimiendo ... ")
        print(f"numero ordenados: {self.numero1}, {self.numero2}, {self.numero3}")
        print(f"El mayor es {self.numero3}")

if __name__ == "__main__":
    numero1, numero2, numero3 = 0, 0, 0
    numeros = OrdenarTresNumeros(numero1, numero2, numero3)
    numeros.ingreser_numeros()
    numeros.ordenar_numeros()
    numeros.imprimir()