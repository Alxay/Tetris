import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((350,700))
clock = pygame.time.Clock()
running = True
gameBoard = np.zeros((20,10),dtype=int)
print(gameBoard)


def generatePiece():
    piece = np.zeros((20,10),dtype=int)
    piece[0][1] = 1
    piece[0][2] = 1
    piece[0][3] = 1
    piece[1][2] = 1
    return piece
   

def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 350, blockSize):
        for y in range(0, 700, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "green", rect, 1)

def drawBoard(gameBoard,piece=np.zeros((20,10),dtype=int)):
    blocks = np.vstack((
        np.argwhere(gameBoard == 1),
        np.argwhere(piece == 1)
    ))
    #[[i j],[i j]]
    for i,j in blocks:
        print(f"Klocek {j}, {i}")
        rect = pygame.Rect(j*35,i*35,35,35)
        pygame.draw.rect(screen,"purple",rect)
        

def move(gameBoard,piece):
    gameBoardBlocks = np.argwhere(gameBoard == 1)
    pieceBlocks = np.argwhere(piece == 1)
    gameBoardBlocks = set(map(tuple, gameBoardBlocks))
    piece2 = np.zeros((20,10),dtype=int)
    for i,j in pieceBlocks:
        if(i >= 19 or (i+1,j) in gameBoardBlocks):
            print("Block under the piece !!")
            
        else:
            piece2[i+1][j] = 1
            piece[i][j] = 0
        
    return piece2



piece = generatePiece()
gameBoard[19][0] = 1
gameBoard[19][1] = 1
gameBoard[10][2] = 1
while running:
    #game loop
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        screen.fill("green")

    drawGrid()
    piece = move(gameBoard,piece)
    print(piece)
    print("-----")
    print(gameBoard)
    drawBoard(gameBoard,piece)
    pygame.display.flip()
    clock.tick(1)




pygame.quit()