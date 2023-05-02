import pygame
from ChessMain import *
#from ChessEngine import *
pygame.init()

#window = pygame.display.set_mode((1300, 800))
#window.fill((255, 255, 255))

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow(screen):
    screen.fill(pygame.Color("white"))
    SAVEbutton.draw(screen, (0, 0, 0))
    NEWbutton.draw(screen, (0, 0, 0))
    SEARCHbutton.draw(screen, (0, 0, 0))
    ENGINEbutton.draw(screen, (0, 0, 0))
    COLOURTHEMESbutton.draw(screen, (0, 0, 0))
    PIECESTHEMESbutton.draw(screen, (0, 0, 0))
    VISUALISATIONGAMEbutton.draw(screen, (0, 0, 0))


run = True
SAVEbutton = button((192, 192, 192), 50, 600, 100, 50, 'SAVE')
NEWbutton = button((192, 192, 192), 175, 600, 100, 50, 'NEW')
SEARCHbutton = button((192, 192, 192), 300, 600, 100, 50, 'SEARCH')
ENGINEbutton = button((192, 192, 192), 425, 600, 100, 50, 'ENGINE')
COLOURTHEMESbutton = button((192, 192, 192), 550, 600, 200, 50, 'COLOUR THEMES')
PIECESTHEMESbutton = button((192, 192, 192), 775, 600, 200, 50, 'PIECES THEMES')
VISUALISATIONGAMEbutton = button((192, 192, 192), 1000, 600, 250, 50, 'VISUALISATION GAME')

while run:
    #redrawWindow(screen)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if SAVEbutton.isOver(pos):
                print('clicked')
            if NEWbutton.isOver(pos):
                print('clicked')
            if SEARCHbutton.isOver(pos):
                print('clicked')
            if ENGINEbutton.isOver(pos):
                print('clicked')
            if COLOURTHEMESbutton.isOver(pos):
                print('clicked')
            if PIECESTHEMESbutton.isOver(pos):
                print('clicked')
            if VISUALISATIONGAMEbutton.isOver(pos):
                print('clicked')

        if event.type == pygame.MOUSEMOTION:
            if SAVEbutton.isOver(pos):
                SAVEbutton.color = (153, 153, 255)
            else:
                SAVEbutton.color = (192, 192, 192)
            if NEWbutton.isOver(pos):
                NEWbutton.color = (153, 153, 255)
            else:
                NEWbutton.color = (192, 192, 192)

            if SEARCHbutton.isOver(pos):
                SEARCHbutton.color = (153, 153, 255)
            else:
                SEARCHbutton.color = (192, 192, 192)

            if ENGINEbutton.isOver(pos):
                ENGINEbutton.color = (153, 153, 255)
            else:
                ENGINEbutton.color = (192, 192, 192)

            if COLOURTHEMESbutton.isOver(pos):
                COLOURTHEMESbutton.color = (153, 153, 255)
            else:
                COLOURTHEMESbutton.color = (192, 192, 192)

            if PIECESTHEMESbutton.isOver(pos):
                PIECESTHEMESbutton.color = (153, 153, 255)
            else:
                PIECESTHEMESbutton.color = (192, 192, 192)

            if VISUALISATIONGAMEbutton.isOver(pos):
                VISUALISATIONGAMEbutton.color = (153, 153, 255)
            else:
                VISUALISATIONGAMEbutton.color = (192, 192, 192)


