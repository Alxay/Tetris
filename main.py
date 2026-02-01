import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((350,700))
clock = pygame.time.Clock()
running = True
gameBoard = np.zeros((20,10),dtype=int)
print(gameBoard)

def generatePiece(gameBoard):
    piece = np.zeros((20,10),dtype=int)
    piece[0][1] = 1
    piece[0][2] = 1
    piece[0][3] = 1
    piece[1][2] = 1
    gameBoard = np.maximum(gameBoard,piece)
    print(gameBoard)
    return gameBoard

def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 350, blockSize):
        for y in range(0, 700, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "green", rect, 1)

def drawBoard(gameBoard):
    blocks = np.argwhere(gameBoard == 1)
    for i,j in blocks:
        print(f"Klocek {i}, {j}")


gameBoard = generatePiece(gameBoard)
drawBoard(gameBoard)
while running:
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        screen.fill("green")

    drawGrid()
    pygame.display.flip()
    clock.tick(60)




pygame.quit()