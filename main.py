import pygame as py
from pygame.locals import *
from Assets.Colors import *


def mein():
    py.init()
    running = True
    screen = py.display.set_mode((940, 640))

    scoreE, scoreP = 0, 0
    font = py.font.Font(None, 73)

    x = 470
    y = 320
    speed = [0, 10]
    ballS = [5, 5]

    playa = Rect(870, 260, 20, 120)  # Player
    enemy = Rect(40, 260, 20, 120)  # Enemy

    screen.fill(BLACK)
    py.draw.rect(screen, WHITE, playa)
    py.draw.rect(screen, WHITE, enemy)
    py.draw.circle(screen, WHITE, (x, y), 15)

    py.display.flip()

    while running:
        for event in py.event.get():
            if event.type == QUIT:
                running = False
                break

        # Player moving
        keys = py.key.get_pressed()
        if keys[py.K_UP] and playa.top > 0:
            speed[1] = -10
            playa = playa.move(speed)
        elif keys[py.K_DOWN] and playa.bottom < 640:
            speed[1] = 10
            playa = playa.move(speed)

        # Enemy moving
        keys = py.key.get_pressed()
        if keys[py.K_w] and enemy.top > 0:
            speed[1] = -10
            enemy = enemy.move(speed)
        elif keys[py.K_s] and enemy.bottom < 640:
            speed[1] = 10
            enemy = enemy.move(speed)

        # Ball touched someone
        if playa.collidepoint((x, y)) or enemy.collidepoint((x, y)):
            ballS[0] *= -1
            x += ballS[0]
            if y >= 640 or y <= 0:
                ballS[1] *= -1
            x += ballS[0]
            y += ballS[1]
        else:
            if x >= 940 or x <= 0:
                ballS[0] *= -1
            elif y >= 640 or y <= 0:
                ballS[1] *= -1
            x += ballS[0]
            y += ballS[1]

        screen.fill(BLACK)

        py.draw.rect(screen, WHITE, playa)
        py.draw.rect(screen, WHITE, enemy)
        py.draw.circle(screen, WHITE, (x, y), 15)

        if x == 0:
            scoreP += 1
            screen.blit(font.render(str(scoreP), True, WHITE), (600, 50))
        elif x == 640:
            scoreE += 1
            screen.blit(font.render(str(scoreE), True, WHITE), (300, 50))
        else:
            screen.blit(font.render(str(scoreE), True, WHITE), (600, 50))
            screen.blit(font.render(str(scoreP), True, WHITE), (300, 50))

        py.display.flip()

        py.time.Clock().tick(60)

    py.quit()


if __name__ == '__main__':
    mein()
