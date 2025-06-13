import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# lets add background
# add images 
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomright = (600,300))



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface,(0,300))

	player_rect.right += 4
	snail_rect.x -= 4
	screen.blit(player_surf,player_rect)
	screen.blit(snail,snail_rect)
	if snail_rect.right <= -200:
		snail_rect.left = 1000
	pygame.display.update()
	clock.tick(60)