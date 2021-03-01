import pygame
import os
import random
import sys


def load_image(name, color_1=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_1 is not None:
        image = image.convert()
        if color_1 == -1:
            color_1 = image.get_at((0, 0))
        image.set_color_1(color_1)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = None
    image_boom = None

    def __init__(self, *group, size=(500, 500)):
        super().__init__(*group)
        if Bomb.image is None:
            Bomb.image = load_image("bomb2.png")
            Bomb.image_boom = load_image("boom.png")
        self.image = Bomb.image
        width, height = size
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.image.get_rect().width)
        self.rect.y = random.randrange(height - self.image.get_rect().height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


def main():
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Boom them all')
    all_sprites = pygame.sprite.Group()
    for i in range(20):
        Bomb(all_sprites, size=size)
    work = True
    while work:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.fill(pygame.Color("black"))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()