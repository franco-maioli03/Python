import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Sacar los comentarios de las id para utilizarlas
#Voz en español femenina
idvoice = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
# Voz en ingles masculina
# idvoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
# Voz en ingles femenina
# idvoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


#Escuchar a nuestro microfono y devolverlo como texto
def transformar_audio():
    #Almacenar el recognizer en variable
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        print('Di algo...')
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='es-ES')
            print('Tú:', texto)
            return texto
        except sr.UnknownValueError:
            return'No se pudo entender el audio'
        except sr.RequestError as e:
            return 'Error en la solicitud:'
        except Exception as ex:
            return 'Error no identificado:'
#Funcion para que el asistente hable
def hablar(mensaje):

    #Encender pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', idvoice)

    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
#Funcion para dar el dia
def pedir_dia():
    #Crear variable con datos de hoy
    dia = datetime.date.today()

    #Crear variable para el dia de la semana
    dia_semana = dia.weekday()

    #Diccionario con nombre de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    #Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')
#Funcion de pedir la hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento, son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)
#Funcion de saludo inicial
def saludo():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    hablar(f'Hola, {momento}, soy tu Asistente personal. Por favor, dime en que te puedo ayudar ')
#Funcion central
def orden():
    saludo()

    comenzar = True
    while comenzar:
        pedido = transformar_audio().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Esto es lo que he encontrado: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Estoy buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar ('Perfecto, Voy a empezar a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precioactual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precioactual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Fue un gusto, nos vemos!')
            break

orden()
    
