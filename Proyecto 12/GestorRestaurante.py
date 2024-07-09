from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

#Funciones
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = resultado

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_bebida + sub_total_comida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postre, 2)}")
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 10000)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*84 + '\n')
    texto_recibo.insert(END, 'Items\t\t\tCant\t\tCosto Items\n')
    texto_recibo.insert(END, f'-'*105 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t\t{comida.get()}\t\t' 
                                     f'${int(comida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t\t{bebida.get()}\t\t' 
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t\t{postre.get()}\t\t' 
                                     f'${int(postre.get()) * precios_bebida[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-'*105 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postre: \t\t\t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-'*105 + '\n')
    texto_recibo.insert(END, f'Sub-total: \t\t\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*'*84 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def reset():
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for y in variables_comida:
        y.set(0)
    for y in variables_bebidas:
        y.set(0)
    for y in variables_postre:
        y.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_impuestos.set('')
    var_subtotal.set('')
    var_total.set('')

#Iniciar tkinter
app = Tk()

#Tamaño de la pantalla
app.geometry('1020x630+0+0')

#Evitar maximizar
app.resizable(0,0)

#Titulo de la ventana
app.title("Mi restaurante - Sistema de Facturacion")

#Color de fondo de la ventana
app.config(bg='aquamarine3')

#Panel superior
panel_superior = Frame(app, bd=1, relief= RIDGE)
panel_superior.pack(side=TOP)

#Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='dark slate gray',
                        font=('Arial', 44), bg='aquamarine3', width=27)
etiqueta_titulo.grid(row=0, column=0)

#Panel Izquierdo
panel_izquierdo = Frame(app, bd=1, relief=RIDGE)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=RIDGE, bg='dark slate gray')
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Arial', 10, 'bold'),
                           bd=1, relief= RIDGE, fg='dark slate gray')
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Arial', 10, 'bold'),
                           bd=1, relief= RIDGE, fg='dark slate gray')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Arial', 10, 'bold'),
                           bd=1, relief= RIDGE, fg='dark slate gray')
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha = Frame(app, bd=1, relief=RIDGE)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=RIDGE, bg='aquamarine3')
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=RIDGE, bg='aquamarine3')
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=RIDGE, bg='aquamarine3')
panel_botones.pack()

#Lista de Productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1','pizza2','pizza3']
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza1','cerveza2']
lista_postres = ['helado','fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']


#Generar items comida
variables_comida= []
cuadros_comida = []
texto_comida =[]
contador = 0
for comida in lista_comidas:

    #Crear CkeckButton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Arial', 10, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    #Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                     font=('Arial', 10, 'bold'),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1) 
    contador += 1


#Generar items bebidas
variables_bebidas= []
cuadros_bebida = []
texto_bebida =[]
contador = 0
for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, 
                          text=bebidas.title(), 
                          font=('Arial', 10, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_bebidas[contador],
                         command=revisar_check)
    bebidas.grid(row=contador, 
                 column=0, 
                 sticky=W)
    #Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                     font=('Arial', 10, 'bold'),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1) 
    contador += 1

#Generar items postre
variables_postre= []
cuadros_postre = []
texto_postre =[]
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre.title(), 
                         font=('Arial', 10, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    #Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, 
                                     font=('Arial', 10, 'bold'),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1) 
    contador += 1

#Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

#Etiqueta de costo y campos de entrada

#Campo Coste de Comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)

#Campo Coste de Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)

#Campo Coste de Postre
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1,padx=41)

#Campo de Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)

#Campo de Impuestos
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_impuestos.grid(row=1,column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1,column=3,padx=41)

#Campo de Total
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Arial', 9, 'bold'),
                              bg='dark slate gray',
                              fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                           font=('Arial', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)

#Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Arial', 10, 'bold'),
                   fg='white',
                   bg='dark slate gray',
                   bd=1,
                   width=9)
    
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)

#Area de Recibo
texto_recibo = Text(panel_recibo,
                    font=('Arial', 10, 'bold'),
                    bd=1,
                    width=60,
                    height=10)
texto_recibo.grid(row=0,column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Arial', 16, 'bold'),
                          width=35,
                          bd=1,)

visor_calculadora.grid(row=0,column=0,columnspan=4)

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','*','=','Borrar','0','/']

botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Arial', 14, 'bold'),
                   fg='white',
                   bg='dark slate gray',
                   bd=1,
                   width=8)
    
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna=0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


#Evitar que se cierre
app.mainloop()