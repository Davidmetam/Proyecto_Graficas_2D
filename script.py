import pygame

pygame.init()
ancho, alto = 800, 700
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Casita UP David Mendoza")

def dibujar_casa():
    # techo
    pygame.draw.polygon(ventana, (175, 103, 79, 255),
                        [(215, 231 + extra), (605, 231 + extra), (645, 335 + extra), (175, 335 + extra)])
    pygame.draw.polygon(ventana, (0, 0, 0, 0),
                        [(215, 231 + extra), (605, 231 + extra), (645, 335 + extra), (175, 335 + extra)], 1)
    pygame.draw.polygon(ventana, (255, 219, 6, 255),
                        [(256, 248 + extra), (295, 195 + extra), (327, 242 + extra), (326, 305 + extra),
                         (256, 305 + extra)])
    pygame.draw.polygon(ventana, (0, 0, 0, 0),
                        [(256, 248 + extra), (295, 195 + extra), (327, 242 + extra), (326, 305 + extra),
                         (256, 305 + extra)], 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (256, 288 + extra), (326, 288 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (256, 272 + extra), (326, 272 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (256, 254 + extra), (326, 254 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (263, 240 + extra), (326, 240 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (275, 224 + extra), (314, 224 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (282, 212 + extra), (308, 212 + extra), 1)
    pygame.draw.polygon(ventana, (255, 255, 255, 255),
                        [(238, 250 + extra), (295, 178 + extra), (351, 250 + extra), (335, 254 + extra),
                         (295, 195 + extra), (253, 254 + extra)])
    pygame.draw.line(ventana, (153, 95, 84, 255), (238, 250 + extra), (295, 178 + extra), 4)
    pygame.draw.line(ventana, (153, 95, 84, 255), (295, 178 + extra), (351, 250 + extra), 4)
    pygame.draw.line(ventana, (0, 0, 0, 0), (351, 250 + extra), (335, 254 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (334, 254 + extra), (294, 195 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (294, 195 + extra), (253, 254 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (253, 254 + extra), (238, 250 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (245, 254 + extra), (295, 188 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (295, 188 + extra), (341, 250 + extra), 1)
    pygame.draw.rect(ventana, (224, 83, 38, 255), pygame.Rect(373, 147 + extra, 31, 84))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(373, 147 + extra, 31, 84), 1)
    pygame.draw.rect(ventana, (224, 83, 38, 255), pygame.Rect(370, 142 + extra, 37, 6))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(370, 142 + extra, 37, 6), 1)

    # porche
    pygame.draw.polygon(ventana, (241, 137, 52, 255),
                        [(220, 390 + extra), (390, 390 + extra), (390, 530 + extra), (220, 530 + extra)])
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 520 + extra), (390, 520 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 504 + extra), (390, 504 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 489 + extra), (390, 489 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 474 + extra), (390, 474 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 459 + extra), (390, 459 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 442 + extra), (390, 442 + extra), 1)
    pygame.draw.line(ventana, (161, 107, 63, 255), (220, 426 + extra), (390, 426 + extra), 1)
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(210, 335 + extra, 10, 196))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(210, 335 + extra, 10, 196), 1)
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(220, 391 + extra, 170, 5))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(220, 413 + extra, 170, 5))

    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(384, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(372, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(360, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(348, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(335, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(322, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(308, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(278, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(266, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(254, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(241, 396 + extra, 5, 17))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(227, 396 + extra, 5, 17))
    pygame.draw.line(ventana, (0, 0, 0, 0), (220, 391 + extra), (390, 391 + extra), 1)

    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(220, 505 + extra, 70, 5))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(227, 508 + extra, 5, 23))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(243, 508 + extra, 5, 23))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(259, 508 + extra, 5, 23))
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(272, 508 + extra, 5, 23))

    pygame.draw.rect(ventana, (127, 82, 17, 255), pygame.Rect(310, 434 + extra, 64, 97))
    pygame.draw.rect(ventana, (151, 33, 21, 255), pygame.Rect(318, 442 + extra, 48, 89))
    pygame.draw.rect(ventana, (81, 20, 15, 255), pygame.Rect(331, 454 + extra, 21, 18))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(331, 454 + extra, 21, 18), 1)
    pygame.draw.circle(ventana, (61, 17, 8, 255), (324, 495 + extra), 3)

    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(249, 440 + extra, 5, 62))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(285, 440 + extra, 5, 62))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(249, 435 + extra, 41, 5))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(245, 490 + extra, 46, 5))
    pygame.draw.rect(ventana, (173, 157, 82, 255), pygame.Rect(254, 440 + extra, 31, 50))
    pygame.draw.rect(ventana, (154, 76, 124, 255), pygame.Rect(254, 440 + extra, 31, 50), 2)
    pygame.draw.line(ventana, (154, 76, 124, 255), (254, 466 + extra), (284, 466 + extra), 3)

    # escaleras
    pygame.draw.rect(ventana, (215, 148, 17, 255), pygame.Rect(205, 530 + extra, 185, 12))
    pygame.draw.rect(ventana, (236, 107, 164, 255), pygame.Rect(209, 542 + extra, 181, 36))
    pygame.draw.rect(ventana, (254, 217, 38, 255), pygame.Rect(216, 549 + extra, 175, 22))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(216, 549 + extra, 175, 22), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (209, 542 + extra), (390, 542 + extra), 1)
    pygame.draw.rect(ventana, (99, 71, 23, 255), pygame.Rect(293, 549 + extra, 98, 36))
    pygame.draw.rect(ventana, (253, 235, 137, 255), pygame.Rect(293, 549 + extra, 97, 6))
    pygame.draw.rect(ventana, (253, 235, 137, 255), pygame.Rect(293, 561 + extra, 97, 6))
    pygame.draw.rect(ventana, (253, 235, 137, 255), pygame.Rect(293, 573 + extra, 97, 6))
    pygame.draw.rect(ventana, (253, 235, 137, 255), pygame.Rect(282, 530 + extra, 11, 59))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(282, 530 + extra, 11, 59), 1)

    # parte azul
    pygame.draw.polygon(ventana, (167, 191, 227, 255),
                        [(220, 336 + extra), (412, 336 + extra), (412, 390 + extra), (220, 390 + extra)])

    pygame.draw.line(ventana, (126, 150, 154, 255), (220, 356 + extra), (409, 356 + extra), 1)
    pygame.draw.line(ventana, (126, 150, 154, 255), (220, 373 + extra), (390, 373 + extra), 1)
    pygame.draw.rect(ventana, (250, 217, 86, 255), pygame.Rect(290, 335 + extra, 10, 196))
    pygame.draw.rect(ventana, (0, 0, 0, 0), pygame.Rect(290, 335 + extra, 10, 196), 1)
    pygame.draw.line(ventana, (110, 86, 58, 255), (175, 335 + extra), (644, 335 + extra), 5)
    # frontal
    pygame.draw.rect(ventana, (200, 212, 52, 255), pygame.Rect(442, 384 + extra, 106, 210))
    pygame.draw.rect(ventana, (162, 199, 42, 255), pygame.Rect(390, 384 + extra, 52, 210))
    pygame.draw.rect(ventana, (232, 255, 21, 255), pygame.Rect(548, 384 + extra, 50, 210))
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 395 + extra), (547, 395 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 412 + extra), (547, 412 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 431 + extra), (547, 431 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 449 + extra), (547, 449 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 467 + extra), (547, 467 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 485 + extra), (547, 485 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 503 + extra), (547, 503 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 537 + extra), (547, 537 + extra), 1)
    pygame.draw.line(ventana, (145, 165, 40, 255), (442, 556 + extra), (547, 556 + extra), 1)
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(442, 519 + extra, 105, 8))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(454, 406 + extra, 82, 12))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(454, 418 + extra, 10, 125))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(526, 418 + extra, 10, 125))
    pygame.draw.rect(ventana, (247, 237, 126, 255), pygame.Rect(464, 418 + extra, 62, 101))
    pygame.draw.rect(ventana, (154, 76, 124, 255), pygame.Rect(464, 418 + extra, 62, 101), 3)
    pygame.draw.line(ventana, (154, 76, 124, 255), (464, 471 + extra), (525, 471 + extra), 5)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 401 + extra), (441, 395 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 417 + extra), (441, 412 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 433 + extra), (441, 431 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 451 + extra), (441, 449 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 467 + extra), (441, 467 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 485 + extra), (441, 485 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 503 + extra), (441, 503 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 537 + extra), (441, 537 + extra), 1)
    pygame.draw.line(ventana, (121, 151, 37, 255), (390, 554 + extra), (441, 556 + extra), 1)
    pygame.draw.rect(ventana, (196, 144, 26, 255), pygame.Rect(390, 519 + extra, 52, 8))
    pygame.draw.rect(ventana, (196, 144, 26, 255), pygame.Rect(396, 422 + extra, 7, 118))
    pygame.draw.rect(ventana, (196, 144, 26, 255), pygame.Rect(430, 419 + extra, 6, 120))
    pygame.draw.polygon(ventana, (196, 144, 26, 255),
                        [(396, 412 + extra), (435, 408 + extra), (435, 419 + extra), (396, 423 + extra)])
    pygame.draw.polygon(ventana, (173, 157, 82, 255),
                        [(403, 423 + extra), (429, 420 + extra), (429, 519 + extra), (403, 519 + extra)])
    pygame.draw.polygon(ventana, (212, 97, 130, 255),
                        [(403, 423 + extra), (429, 420 + extra), (429, 519 + extra), (403, 519 + extra)], 2)
    pygame.draw.line(ventana, (212, 97, 130, 255), (403, 473 + extra), (429, 473 + extra), 4)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 395 + extra), (597, 401 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 412 + extra), (597, 417 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 431 + extra), (597, 433 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 449 + extra), (597, 451 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 467 + extra), (597, 467 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 485 + extra), (597, 485 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 503 + extra), (597, 503 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 537 + extra), (597, 537 + extra), 1)
    pygame.draw.line(ventana, (154, 166, 32, 255), (547, 556 + extra), (597, 554 + extra), 1)
    pygame.draw.rect(ventana, (253, 203, 30, 255), pygame.Rect(547, 519 + extra, 50, 8))
    pygame.draw.rect(ventana, (253, 203, 30, 255), pygame.Rect(555, 418 + extra, 7, 123))
    pygame.draw.rect(ventana, (253, 203, 30, 255), pygame.Rect(585, 422 + extra, 6, 120))
    pygame.draw.polygon(ventana, (253, 203, 30, 255),
                        [(555, 405 + extra), (590, 412 + extra), (590, 424 + extra), (555, 417 + extra)])
    pygame.draw.polygon(ventana, (247, 237, 126, 255),
                        [(562, 417 + extra), (584, 422 + extra), (584, 519 + extra), (562, 519 + extra)])
    pygame.draw.polygon(ventana, (154, 76, 124, 255),
                        [(562, 417 + extra), (584, 422 + extra), (584, 519 + extra), (562, 519 + extra)], 2)
    pygame.draw.line(ventana, (154, 76, 124, 255), (562, 473 + extra), (584, 473 + extra), 4)
    pygame.draw.rect(ventana, (112, 39, 68, 255), pygame.Rect(573, 336 + extra, 25, 20))

    pygame.draw.polygon(ventana, (231, 184, 6, 255),
                        [(380, 365 + extra), (608, 365 + extra), (598, 384 + extra), (390, 384 + extra)])
    pygame.draw.polygon(ventana, (238, 222, 55, 255),
                        [(412, 338 + extra), (572, 338 + extra), (608, 365 + extra), (380, 365 + extra)])
    pygame.draw.rect(ventana, (244, 226, 58, 255), pygame.Rect(412, 268 + extra, 161, 70))
    pygame.draw.polygon(ventana, (250, 240, 51, 255), [(412, 268 + extra), (490, 108 + extra), (573, 268 + extra)])
    pygame.draw.polygon(ventana, (224, 235, 229, 255),
                        [(357, 315 + extra), (490, 66 + extra), (622, 315 + extra), (598, 315 + extra),
                         (490, 108 + extra), (388, 315 + extra)])
    pygame.draw.line(ventana, (153, 95, 84, 255), (357, 315 + extra), (490, 66 + extra), 6)
    pygame.draw.line(ventana, (153, 95, 84, 255), (490, 66 + extra), (622, 315 + extra), 6)
    pygame.draw.line(ventana, (0, 0, 0, 0), (622, 315 + extra), (598, 315 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (598, 315 + extra), (490, 108 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (490, 108 + extra), (388, 315 + extra), 2)
    pygame.draw.line(ventana, (0, 0, 0, 0), (388, 315 + extra), (357, 315 + extra), 2)

    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(449, 298 + extra, 85, 8))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(458, 201 + extra, 67, 10))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(458, 211 + extra, 10, 110))
    pygame.draw.rect(ventana, (253, 208, 91, 255), pygame.Rect(515, 211 + extra, 10, 115))
    pygame.draw.rect(ventana, (247, 237, 126, 255), pygame.Rect(468, 211 + extra, 47, 87))
    pygame.draw.rect(ventana, (154, 76, 124, 255), pygame.Rect(468, 211 + extra, 47, 87), 3)
    pygame.draw.line(ventana, (154, 76, 124, 255), (468, 256 + extra), (514, 256 + extra), 5)

    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(274, 237 + extra, 5, 62))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(310, 237 + extra, 5, 62))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(274, 232 + extra, 41, 5))
    pygame.draw.rect(ventana, (236, 190, 79, 255), pygame.Rect(270, 287 + extra, 46, 5))
    pygame.draw.rect(ventana, (173, 157, 82, 255), pygame.Rect(279, 237 + extra, 31, 50))
    pygame.draw.rect(ventana, (154, 76, 124, 255), pygame.Rect(279, 237 + extra, 31, 50), 2)
    pygame.draw.line(ventana, (154, 76, 124, 255), (279, 263 + extra), (309, 263 + extra), 3)

    pygame.draw.line(ventana, (0, 0, 0, 0), (388, 50 + extra), (388, 142 + extra), 1)
    pygame.draw.circle(ventana, azul, (388, 50 + extra), 20)
    pygame.draw.circle(ventana, negro, (388, 50 + extra), 20, 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (370, 30 + extra), (388, 142 + extra), 1)
    pygame.draw.line(ventana, (0, 0, 0, 0), (405, 27 + extra), (388, 142 + extra), 1)
    pygame.draw.circle(ventana, rojo, (370, 30 + extra), 20)
    pygame.draw.circle(ventana, negro, (370,30 + extra), 20, 1)
    pygame.draw.circle(ventana, amarillo, (405, 27 + extra), 20)
    pygame.draw.circle(ventana, negro, (405, 27 + extra), 20, 1)

azul = "#065c9c"
rojo = "#ff1a00"
amarillo = "#ffc927"
negro = "#000000"

extra = 70
Corriendo = True

while Corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Corriendo = False
        ventana.fill(("#cae1f2"))

        dibujar_casa()
        pygame.display.update()

pygame.quit()
