class NumeroComplejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = '+' if self.imaginario >= 0 else '-'
        return f"{self.real} {signo} {abs(self.imaginario)}i"

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def dividir(self, otro):
        divisor = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return NumeroComplejo(real, imaginario)

# Ejemplo de uso
c1 = NumeroComplejo(3, 2)
c2 = NumeroComplejo(1, 7)

print("Suma:", c1.sumar(c2))
print("Resta:", c1.restar(c2))
print("Multiplicación:", c1.multiplicar(c2))
print("División:", c1.dividir(c2))
