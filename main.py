import pygame

# pygame setup
pygame.init()
pygame.display.set_caption('Peeking Froggy')
width, height = 150, 150
screen = pygame.display.set_mode((width, height))
# , pygame.NOFRAME
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

frog_image = pygame.image.load('images/froggy.png')
frog_rect = frog_image.get_rect()

frog_rect.top = height - 53
frog_rect.centerx = width // 2


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((173, 216, 230))
    screen.blit(frog_image, frog_rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    hovering = 20 < mouse_x < width -21 and 20 < mouse_y < height -11

    if hovering and frog_rect.top > height - 110:
        frog_rect.move_ip(0, -2)

    elif not hovering and frog_rect.top < height - 53:
        frog_rect.move_ip(0, 1)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
