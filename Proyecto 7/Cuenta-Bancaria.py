import os

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de Cuenta: {self.numero_cuenta}\nBalance: {self.balance}"
    def depositar(self, dinero_depositado):
        self.balance =+ dinero_depositado
        input('Dinero Depositado. Ingrese un caracter para continuar')
    def retirar(self, dinero_retirado):
        if(dinero_retirado > self.balance):
            input(f'Fondos insuficientes. Su saldo es: {self.balance}. Ingrese un caracter para continuar')
        else:
            self.balance =- dinero_retirado
            input('Dinero Retirado. Ingrese un caracter para continuar')
    
        
def crear_cliente():
    nombre_cliente = input('Ingrese su nombre: \n')
    apellido_cliente = input('Ingrese su apellido: \n')
    numero_cuenta_cliente = input('Ingrese su numero de cuenta: \n')
    nueva_cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta_cliente)
    os.system('cls' if os.name == 'nt' else 'clear')
    return nueva_cliente

def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0

    while opcion != 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        opcion = input('Ingrese una opcion:\nDepositar(D), Retirar(R), Salir(S): ')

        if (opcion == 'D') or (opcion == 'd'):
            dinero_depositado = int(input('Ingrese un monto a depositar: '))
            cliente.depositar(dinero_depositado)
        elif (opcion == 'R') or (opcion == 'r'):
            retiro = int(input('Ingrese un monto a retirar: '))
            cliente.retirar(retiro)
        input(cliente)

inicio()


