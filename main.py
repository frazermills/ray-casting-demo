import pygame, math

def main():

    WIDTH = 800
    HEIGHT = 800
    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (220, 0, 0)
    GREEN = (0, 220, 0)
    LIGHT_BLUE = (0, 128, 255)
    GREY = (95, 95, 95)
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ray-casting demo - by Frazer Mills")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)

        pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(screen, GREY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
