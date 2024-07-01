#Archivo para incializar el programa

import numeros

nuevo = 'si'

# Se repite el codigo hasta que se responda algo diferente a 'si'

while nuevo.lower() == 'si':
    sector = input("Bienvenido a el Turneo de nuestro Farmacia. De que sector quiere un turno?\nP. Perfumeria\nF. Farmacia\nC. Cosmeticos\n").upper()

    numeros.decorador(sector)

    nuevo = input('¿Quiere realizar otra orden? (si/no): ')

nuevo = 'si'  # Inicializar con 'si' para que entre al ciclo while al menos una vez

if nuevo.lower() == 'no':
    print('Debe responder con si o no')
    nuevo = input('¿Quiere realizar otra orden? (si/no): ')