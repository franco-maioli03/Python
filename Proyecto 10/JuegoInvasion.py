import pygame
import random
import math
from pygame import mixer

#Inicializo Pygame
pygame.init()

#Creo la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono del juego
pygame.display.set_caption("Invasión Alienigena")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

#Musica y Sonidos
mixer.music.load("musica-peliculas-15-.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)
bala_ruido = "scifi002.mp3"
impacto_sonido = "003576076_prev.mp3"

#Variables del Jugador
img_jugador = pygame.image.load("enemigo.png")
jugador_x = 384
jugador_y = 550
jugador_x_cambio = 0

#Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("astronave.png"))
    enemigo_x.append(random.randint(0, 768))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

#Variables de la Bala
img_bala = pygame.image.load("disparo.png")
bala_x = 0
bala_y = 550
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#Puntos
puntaje = 0
fuente = pygame.font.Font('Begok v15_2015___free.ttf', 32)
texto_x = 30
texto_y = 10

#texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60, 200))

#Funcion para mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"PPuntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x, y))


#Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

#Funcion Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#Funcion disparar Bala
def dispara(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 4, y + 10))

#Funcion de colisiones
def colision(x_1, y_1, x_2, y_2):
    dis = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if dis < 27:
        return True
    else:
        return False

#Loop del juego
ejecutar = True
while ejecutar:
    #Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    #Iterarar eventos
    for evento in pygame.event.get():
        #Evento de cerrar el programa
        if evento.type == pygame.QUIT:
            ejecutar = False
        
        #Evento de apretar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                ruido_bala = mixer.Sound(bala_ruido)
                ruido_bala.set_volume(0.3)
                ruido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    dispara(bala_x, bala_y)
        
        #Evento de soltar las flecas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Modificar ubicacion del Jugador
    jugador_x += jugador_x_cambio

    #Mantener dentro de la pantalla al Jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 768:
        jugador_x = 768

    #Modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        #Final del Juego
        if enemigo_y[e] > 525:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    #Mantener dentro de la pantalla al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 768:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        #Impacto
        impacto = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if impacto:
            sonido_impacto = mixer.Sound(impacto_sonido)
            sonido_impacto.set_volume(0.3)
            sonido_impacto.play()
            bala_y = 550
            bala_visible = False
            puntaje += 25
            enemigo_x[e] = random.randint(0, 768)
            enemigo_y[e] = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
            

    #Movimiento de la bala
    if bala_y <= -32:
        bala_y = 550
        bala_visible = False
    
    if bala_visible:
        dispara(bala_x, bala_y)
        bala_y -= bala_y_cambio

    #Llamado a las funciones
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    #Actualizar pantalla
    pygame.display.update()