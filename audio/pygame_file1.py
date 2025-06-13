import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('My Game')

# lets estalish background.
# adding background files.
sky_surf = pygame.image.load("sky.png").convert()
ground_surf = pygame.image.load("ground.png").convert()

 


clock = pygame.time.Clock()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surf,(0,0))
	

	pygame.display.update()
	clock.tick(60)