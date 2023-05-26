import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wolf Eats Rabbit Game")

player_img = pygame.image.load("player.png")
rabbit_img = pygame.image.load("rabbit.png")
background_img = pygame.image.load("background.jpg")
play_button_img = pygame.image.load("play_button.png")

player_size = 50
player_img = pygame.transform.scale(player_img, (player_size, player_size))
player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2
player_speed = 5

rabbit_size = 30
rabbit_img = pygame.transform.scale(rabbit_img, (rabbit_size, rabbit_size))
rabbit_x = random.randint(0, width - rabbit_size)
rabbit_y = random.randint(0, height - rabbit_size)

score = 0
font = pygame.font.Font(None, 36)

menu_font = pygame.font.Font(None, 72)
menu_title = menu_font.render("Wolf Eats Rabbit", True, (255, 255, 255))
menu_title_rect = menu_title.get_rect(center=(width // 2, height // 4))
play_button_rect = play_button_img.get_rect(center=(width // 2, height // 2 + 50))

MENU = 0
GAME = 1
game_state = MENU

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == MENU:
                game_state = GAME
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == MENU:
            mouse_pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                game_state = GAME

    if game_state == GAME:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        if player_x < 0:
            player_x = 0
        elif player_x > width - player_size:
            player_x = width - player_size
        if player_y < 0:
            player_y = 0
        elif player_y > height - player_size:
            player_y = height - player_size

        if player_x < rabbit_x + rabbit_size and player_x + player_size > rabbit_x and player_y < rabbit_y + rabbit_size and player_y + player_size > rabbit_y:
            rabbit_x = random.randint(0, width - rabbit_size)
            rabbit_y = random.randint(0, height - rabbit_size)
            score += 1

        screen.blit(background_img, (0, 0))
        screen.blit(rabbit_img, (rabbit_x, rabbit_y))
        screen.blit(player_img, (player_x, player_y))

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    elif game_state == MENU:
        screen.fill((0, 0, 0))
        screen.blit(menu_title, menu_title_rect)
        screen.blit(play_button_img, play_button_rect)

    pygame.display.flip()

pygame.quit()
