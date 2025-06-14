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


player_gravity = 0



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and player_rect.bottom == 300:
				player_gravity = -20


		if event.type == pygame.MOUSEBUTTONDOWN:
			if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
				player_gravity = -20



		if snail_rect.colliderect(player_rect):
			exit()

		

	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface,(0,300))



	# player_rect.x += 4
	if player_rect.left >= 800:
		player_rect.right = 0
	snail_rect.x -= 20

	
		

	player_gravity += 1
	player_rect.y += player_gravity




	if player_rect.bottom >= 300 :
		player_rect.bottom = 300

	





	screen.blit(player_surf,player_rect)
	screen.blit(snail,snail_rect)
	if snail_rect.right <= -200:
		snail_rect.left = 1000
	pygame.display.update()
	clock.tick(60)