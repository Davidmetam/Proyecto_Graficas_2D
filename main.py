import pygame
from figuras import Figuras
pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Practicas ")
Negro ="#000000"
BLANCO=(255,255,255)
ROJO    = (255, 0, 0)
VERDE   = (0, 255, 0)
NARANJA=(255, 165, 0)
CIAN     = (0, 255, 255)
MORADO   = (128, 0, 128)
AZUL = (0, 0, 255)

dibujador = Figuras(ventana)


Corriendo =True

while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False

        ventana.fill(Negro)
        #dibujador.curva(100,50,300,170,150,ROJO)
        #dibujador.curva(8, 150, 300, 170, 150,ROJO)
        #dibujador.humito(150,300,400,50,40,ROJO)
        #dibujador.curva_parametricamente(100,100,400,50, ROJO)
        #dibujador.infinito(100,350,300,300,ROJO)
        #dibujador.mandala1(300,300,300,100,ROJO)
        #dibujador.mandala2(300,300,300,10,ROJO)

        #puntosX = [110, 120, 130, 140, 150, 160]
        #puntosY = [110, 120, 130, 140, 150, 160]
        #dibujador.mallado(puntosX, puntosY, ROJO)

        # punto_inicial_cubo = [392, 275, 50]
        # longitud_arista = 150
        # punto_proyeccion = [400, 300, 300]
        # dibujador.dibujar_cubo_proyectado(punto_inicial_cubo, longitud_arista, punto_proyeccion, ROJO)

        punto_inicial_cubo = [392, 275, 50]
        longitud_arista = 90
        punto_proyeccion = [140, 30, 30]
        dibujador.dibujar_pixel(140, 30, AZUL)
        dibujador.dibujar_cubo_proyectado(punto_inicial_cubo, longitud_arista, punto_proyeccion, ROJO)

        pygame.display.update()

pygame.quit()