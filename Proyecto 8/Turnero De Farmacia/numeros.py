# Archivo para los generadores y decoradores

# Generadores para los diferentes sectores
def turno_perfumeria():
    x = 0
    while True:
        x += 1
        if x >= 10:
            yield f"P-{x}"
        else:
            yield f"P-0{x}"
def turno_farmacia():
    x = 0
    while True:
        x += 1
        if x >= 10:
            yield f"F-{x}"
        else:
            yield f"F-0{x}"
def turno_cosmeticos():
    x = 0
    while True:
        x += 1
        if x >= 10:
            yield f"C-{x}"
        else:
            yield f"C-0{x}"
        
# Le asigno una variable a cada uno
perfumeria = turno_perfumeria()
farmacia = turno_farmacia()
cosmeticos = turno_cosmeticos()

# Decorador para los sectores para no repetir codigo

def decorador(sector):
    print("\n" + "*" * 20)
    print("Su turno es: ")
    if sector == 'P':
        print(next(perfumeria))
    elif sector == 'F':
        print(next(farmacia))
    elif sector == 'C':
        print(next(cosmeticos))
    print("Aguarde y sera atendido")
    print("*" * 20 + "\n")