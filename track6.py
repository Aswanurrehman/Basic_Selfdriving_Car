import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('Tracks/track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 280
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    car_y = car_y-2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.display.update()