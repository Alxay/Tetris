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
    piece[0][2] = 1
    piece[0][3] = 1
    piece[0][4] = 1
    piece[1][3] = 1
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
        # print(f"Klocek {j}, {i}")
        rect = pygame.Rect(j*35,i*35,35,35)
        pygame.draw.rect(screen,"purple",rect)
        

def frame(gameBoard,piece):
    gameBoardBlocks = np.argwhere(gameBoard == 1)
    pieceBlocks = np.argwhere(piece == 1)
    gameBoardBlocks = set(map(tuple, gameBoardBlocks))
    piece2 = np.zeros((20,10),dtype=int)
    for i,j in pieceBlocks:
        if(i >= 19 or gameBoard[i+1][j] == 1 ):
            print("Block under the piece !!\n")
            # Return gameBoard with piece added
            gameBoard = np.maximum(gameBoard,piece)
            print("Final Game Board:")
            print(gameBoard)
            return generatePiece(),gameBoard
            
        else:
            piece2[i+1][j] = 1
            # piece[i][j] = 0
        
    return piece2,gameBoard

def checkColision(gameBoard,piece):
    if np.any((gameBoard==1)&(piece==1)):
        return True
    return False

def maxCords(blocks):
    minX = 100
    maxX = 0
    minY = 100
    maxY = 0
    for i,j in blocks:
        if i > maxX:
            maxX = i
        if i < minX:
            minX = i
        if j > maxY:
            maxY = j
        if j < minY:
            minY = j
    return minX,maxX,minY,maxY
def move(gameBoard,piece,direction):
    print("ruch")
    pieceBlocks = np.argwhere(piece == 1)
    gameBlocks = np.argwhere(gameBoard == 1)
    print(pieceBlocks)
    minX,maxX,minY,maxY = maxCords(pieceBlocks)
    piece2 = np.zeros((20,10),dtype=int)
    if direction == 1:
        if maxY >= 9:
            return piece,gameBoard
        for i,j in pieceBlocks:
            piece2[i][j+1] = 1
        if checkColision(gameBoard,piece2):
            return piece,gameBoard
        
    if direction == 2:
        if minY <= 0:
            return piece,gameBoard
        for i,j in pieceBlocks:
            piece2[i][j-1] = 1
        if checkColision(gameBoard,piece2):
            return piece,gameBoard
    if direction == 3:
        centerX,centerY = (minX+maxX)//2,(minY+maxY)//2
        print(f"minX: {minX}, maxX: {maxX}, minY: {minY}, maxY: {maxY}")
        print(f"centerX: {centerX}, centerY: {centerY}")
        x1 = max(centerX-1, 0)
        x2 = min(centerX+2, piece.shape[0])
        y1 = max(centerY-1, 0)
        y2 = min(centerY+2, piece.shape[1])

        fragment = piece[x1:x2, y1:y2]
        print(fragment)
        rotated = np.rot90(fragment, -1)  # -1 = 90° w prawo
        print(rotated)
        if minY <= 0 or maxY >= 9 or minX <= 0 or maxX >= 19:
            return piece,gameBoard
        piece2[x1:x2, y1:y2] = rotated

        # try:
        #     piece2[x1:x2, y1:y2] = rotated
        # except ValueError:
        #     print("Nie można wstawić fragmentu – wychodzi poza planszę!")
        #     return piece
        if np.any((gameBoard==1)&(piece2==1)):
            print("Kolizja po obrocie!")
            return piece,gameBoard
        
    return piece2,gameBoard


piece = generatePiece()
gameBoard[19][0] = 1
gameBoard[19][1] = 1
gameBoard[10][2] = 1
# Tworzymy własne ID zdarzenia
TICK_EVENT = pygame.USEREVENT + 1

# Ustaw timer, który wysyła TICK_EVENT co 1000 ms (1 sekunda)
pygame.time.set_timer(TICK_EVENT, 1000)

while running:
    #game loop
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TICK_EVENT:
            print("Tick event received!")
            piece, gameBoard = frame(gameBoard,piece)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        screen.fill("green")
    if keys[pygame.K_d]:
        piece,gameBoard = move(gameBoard,piece,1)
    if keys[pygame.K_a]:
        piece,gameBoard = move(gameBoard,piece,2)
    if keys[pygame.K_w]:
        piece,gameBoard = move(gameBoard,piece,3)    
    if keys[pygame.K_s]:   
        piece, gameBoard = frame(gameBoard,piece)

    
    # print(piece)
    # print("-----")
    # print(gameBoard)
    
    drawGrid()
    drawBoard(gameBoard,piece)
    pygame.display.flip()
    clock.tick(15)




pygame.quit()