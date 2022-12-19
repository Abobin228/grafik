import pygame
a, b = 10, 10
k, m = 40, 100
g, h = 100, 200
e, f = 300, 400
c, d = 400, 440


pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    screen.fill('black')
    pygame.draw.line(screen, 'white', (a, b), (k, m), 10)
    pygame.draw.line(screen, 'white', (k, m), (g, h ) , 10)
    pygame.draw.line(screen, 'white', (g, h), (e, f), 10)
    pygame.draw.line(screen, 'white', (e, f), (c, d), 10)
    pygame.display.flip()
