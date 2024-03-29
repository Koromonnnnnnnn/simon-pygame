import pygame
import random
import math
import winsound

pygame.init()
pygame.display.set_caption("Simon")
screen = pygame.display.set_mode((800, 800))

# main variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
hasClicked = False
pattern = []
playerPattern = []
playerTurn = True
pi = 3.1415
ded = False
gameLoop = True


def collision(xpos, ypos):
    if math.sqrt((xpos - 400) ** 2 + (ypos - 400) ** 2) > 200 or math.sqrt((xpos - 400) ** 2):
        print("Outside of ring")
        return -1
    elif xpos < 400 and ypos < 400:
        print("Over red button")
        pygame.draw.arc(screen, (255, 0, 0),
                        (200, 200, 400, 400), pi/2, pi, 100)
        pygame.display.flip()
        winsound.Beep(440, 500)
        return 0
    elif xpos < 400 and ypos > 400:
        print("Over green button")
        pygame.draw.arc(screen, (0, 255, 0),
                        (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.display.flip()
        winsound.Beep(640, 500)
        return 1


while gameLoop == True:
    event = pygame.event.wait()

    # input
    if event.type == pygame.QUIT:
        gameLoop = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked = True
        print("Click")

    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    # player turn
    if playerTurn == True:
        print("starting player turn")
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
        else:
            playerTurn = False
            pygame.time.wait(800)

    # play computer pattern
    if playerTurn == False:
        print("Starting machine turn")
        pattern.append(random.randrange(0, 4))

        for i in range(len(pattern)):
            if pattern[i] == 0:
                pygame.draw.arc(screen, (255, 0, 0),
                                (200, 200, 400, 400), (pi/2), pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)

            elif pattern[i] == 1:
                pygame.draw.arc(screen, (0, 255, 0),
                                (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)
            elif pattern[i] == 2:
                pygame.draw.arc(screen, (255, 255, 0),
                                (200, 200, 400, 400), (3*pi/2), (0*pi), 100)
                pygame.display.flip()
                winsound.Beep(340, 500)
            elif pattern[i] == 3:
                pygame.draw.arc(screen, (0, 0, 255),
                                (200, 200, 400, 400), (0*pi), (pi/2), 100)
                pygame.display.flip()
                winsound.Beep(240, 500)

        # render section
        pygame.draw.arc(screen, (155, 0, 0),
                        (200, 200, 400, 400), (pi/2), pi, 100)
        pygame.draw.arc(screen, (0, 155, 0),
                        (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.draw.arc(screen, (155, 155, 0), (200, 200,
                                                400, 400), (3*pi/2), (0*pi), 100)
        pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400),
                        (0*pi), (pi/2), 100)
        # game board

        pygame.display.flip()
        pygame.time.wait(800)
        playerTurn = True
        playerPattern.clear()


pygame.quit()
