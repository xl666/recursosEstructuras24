class CuentaBancaria:
    def __init__(self, titular, numero_cuenta):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_informacion(self):
        print("Titular:", self.titular)
        print("Número de cuenta:", self.numero_cuenta)
        print("Saldo:", self.saldo)

if __name__ == "__main__":
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    cuenta = CuentaBancaria(titular, numero_cuenta)
    cuenta.depositar(1000)
    cuenta.mostrar_informacion()
