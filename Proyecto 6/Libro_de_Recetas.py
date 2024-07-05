## Se importan as librerias
from pathlib import Path
import os
from os import system

## Se hacen las funciones necesarias para el codigo

def contador_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador
def mostrar_categorias(ruta):
    print("Categorias: ")
    lista = []
    url = Path(ruta)
    contador = 1
    for carpeta in url.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"{contador} - {carpeta_str}")
        lista.append(carpeta)
        contador += 1
    return lista
def elegir_categoria(lista):
    eleccion = ''
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElije una categoria: ")
    return lista[int(eleccion) - 1]
def mostrar_recetas(ruta):
    print("Recetas: ")
    lista_resetas = []
    ruta_recetas = Path(ruta)
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"{contador} - {receta_str}")
        lista_resetas.append(receta)
        contador += 1
    return lista_resetas
def elegir_receta(lista):
    eleccion = ''
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElije una receta: ")
    return lista[int(eleccion) - 1]
def crear_categoria(ruta):
    repetir = '1'
    while repetir != '2':
        existe = False
        if repetir == '1':
            while not existe:
                nuevo_nombre_categoria= input('Escribe el nombre de la nueva categoria: ')
                nueva_ruta = Path(ruta, nuevo_nombre_categoria)
                if not os.path.exists(nueva_ruta):
                    Path.mkdir(nueva_ruta)
                    input(f'La nueva categoria: {nuevo_nombre_categoria} fue creada. Ingrese un caracter para continuar: ')
                    existe = True
                    os.system('cls' if os.name=='nt' else 'clear')
                else:
                    print('Esa categoria ya fue creada')
        repetir = input("Quieres agregar alguna categoria?\nResponder con un numero como opción:\n1. Si\n2. No\n")
def crear_receta(ruta):
    repetir = '1'
    while repetir != '2':
        existe = False
        if repetir == '1':
            while not existe:
                nuevo_nombre_receta = input('Escribe el nombre de la nueva receta: ') + '.txt'
                nuevo_contenido_receta = input('Escribe el contenido de la nueva receta: \n')
                nueva_ruta = Path(ruta, nuevo_nombre_receta)

                if not os.path.exists(nueva_ruta):
                    Path.write_text(nueva_ruta, nuevo_contenido_receta)
                    print(f'La nueva receta: {nuevo_nombre_receta} fue creada')
                    input('Ingrese un caracter para continuar: ')
                    os.system('cls' if os.name=='nt' else 'clear')
                    existe = True
                else:
                    print('Esa receta ya fue creada')
        repetir = input("Quieres agregar alguna receta?\nResponder con un numero como opción:\n1. Si\n2. No\n")
def eliminar_receta(receta):
        repetir = input(f"Estas seguro de eliminar {receta.name}?\nResponder con un numero como opción:\n1. Si\n2. No\n")
        if repetir == '1':
            Path(receta).unlink()
            input(f'La receta {receta.name} fue eliminada. Ingrese un caracter para continuar: ')
        if repetir == '2':
            input('La accion fue cancelada. Ingrese un caracter para continuar: ')
def eliminar_categoria(categoria):
        repetir = input(f"Estas seguro de eliminar {categoria.name }?\nResponder con un numero como opción:\n1. Si\n2. No\n")
        if repetir == '1':
            Path(categoria).rmdir()
            input(f'La categoria {categoria.name} fue eliminada. Ingrese un caracter para continuar: ')
        if repetir == '2':
            input('La accion fue cancelada. Ingrese un caracter para continuar: ')


## Saludo de Bienvenida
print('Bienvenido a el libro de recetas')
ruta = Path(Path.home(), "OneDrive - ITX Corp", "Desktop", "Python", "Recetas")
ruta_recetas = os.path.dirname("C:\\Users\\fmaioli\\OneDrive - ITX Corp\\Desktop\\Python\\Recetas\\Carnes")
print("Este libro se encuentra en: " + ruta_recetas)

print(f"Este libro tiene {contador_recetas(ruta_recetas)} recetas")

input("Presione algun boton para continuar: ")

## Fin de la Bienvenida

## Se muestra el menu principal que se repite hasta que se decida salir del loop while

os.system('cls' if os.name=='nt' else 'clear')

## Comienza el ciclo while
opcion = 0
while opcion != '6':
    opcion = input("""Elija alguna de las opciones
        1. Leer Receta
        2. Crear Receta
        3. Crear Categoria
        4. Eliminar Receta
        5. Eliminar categoria
        6. Cerrar libro de Recetas
        Su opcion es: """)
    os.system('cls' if os.name=='nt' else 'clear')

##Mostramos lo que sucede en el primer caso (Leer Receta)
    if opcion == '1':
        receta = elegir_receta(mostrar_recetas(elegir_categoria(mostrar_categorias(ruta))))
        print(receta.read_text())
        input('Ingrese un caracter para continuar: ')
        os.system('cls' if os.name=='nt' else 'clear')
        
    if opcion == '2':
        crear_receta(elegir_categoria(mostrar_categorias(ruta)))
        os.system('cls' if os.name=='nt' else 'clear')
        
    if opcion == '3':
        crear_categoria(ruta)
        os.system('cls' if os.name=='nt' else 'clear')

    if opcion == '4':
        eliminar_receta(elegir_receta(mostrar_recetas(elegir_categoria(mostrar_categorias(ruta)))))
        os.system('cls' if os.name=='nt' else 'clear')
    
    if opcion == '5':
        eliminar_categoria(elegir_categoria(mostrar_categorias(ruta)))
        os.system('cls' if os.name=='nt' else 'clear')