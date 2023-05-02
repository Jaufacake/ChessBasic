#This section is responsible for handing user input and displaying current game state evaluation.
import pygame as p
from PyQt5 import QtCore
from Chess import ChessEngine, Chess_AI
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel, QButtonGroup, QMainWindow, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
import PyQt5.QtWidgets as qtw
from multiprocessing import Process, Queue


WIDTH = HEIGHT = 512
DIMENSION = 8  #Dimensions of a chess board is 8x8
MOVE_LOG_PANEL_WIDTH = 448
MOVE_LOG_PANEL_HEIGHT = 787
CONTROL_PANEL_WIDTH = 800
CONTROL_PANEL_HEIGHT = 300
spacing = 100
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  #For animations later on
IMAGES = {}

"""
Different themes for the colours of the board
"""

RED_CHECK = (240, 150, 150)
WHITE = (255, 255, 255)
BLUE_LIGHT = (140, 184, 219)
BLUE_DARK = (91, 131, 159)
GREY_LIGHT = (240, 240, 240)
GREY_DARK = (200, 200, 200)
LIGHT = (212, 202, 190)
DARK = (100, 92, 89)
LICHESS_LIGHT = (240, 217, 181)
LICHESS_DARK = (181, 136, 99)
LICHESS_GREY_LIGHT = (164, 164, 164)
LICHESS_GREY_DARK = (136, 136, 136)

BOARD_COLOURS = [(GREY_LIGHT, GREY_DARK), (BLUE_LIGHT, BLUE_DARK), (WHITE, RED_CHECK),
                 (LIGHT, DARK), (LICHESS_LIGHT, LICHESS_DARK), (LICHESS_GREY_LIGHT, LICHESS_GREY_DARK)]

global board_colour
board_colour = (LICHESS_LIGHT, LICHESS_DARK)

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''

#this is loading the images that have been stored part of this file and matching them to the piece name, e.g. 'wp'
def loadImages():
    #We can access an image by saying 'IMAGES['wp']'
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
'''
This will handle user input and updating the graphics 
'''

def main():
    p.init()
    screen = p.display.set_mode((1200, 640), p.RESIZABLE)
    screen.fill(p.Color("white"))

    p.display.set_caption("ChessBasics")
    icon = p.image.load('/Users/nadiajaufarally/PycharmProjects/pythonChessProject/Chess/images/Icon/pawn.png')
    p.display.set_icon(icon)

    def SaveScreen():
        class Ui_MainWindow(QtWidgets.QWidget):
            def setupUi(self, MainWindow):
                MainWindow.resize(422, 255)
                self.centralwidget = QtWidgets.QWidget(MainWindow)

                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(115, 100, 200, 28))

                # For displaying confirmation message along with user's info
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(115, 40, 201, 111))

                self.label.setText("")

                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

            def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("SAVE", "SAVE"))

                name, done1 = QtWidgets.QInputDialog.getText(
                    self, 'Your Name', 'Enter your name:')

                oppname, done2 = QtWidgets.QInputDialog.getText(
                    self, "Opponent's Name", "Enter your opponent's name:")

                tournament, done4 = QtWidgets.QInputDialog.getText(
                    self, 'Tournament Title', "Enter the Tournament:")

                game_date, done5 = QtWidgets.QInputDialog.getText(
                    self, 'Date of Game', "Enter the date of the game:")

                result = ['1-0', '0-1', '1/2 -1/2']
                result, done3 = QtWidgets.QInputDialog.getItem(
                    self, 'Result of Game', 'Result of the Game', result)

                if done1 and done2 and done3 and done4 and done5:
                    # Showing confirmation message along
                    # with information provided by user.
                    self.label.setText('Information stored Successfully\nGame Title: '
                                 +str(name)+' VS '+str(oppname)+'\n'+'Tournament: '
                                 +str(tournament)+'\nResult of game: '+str(result)
                                 +'\nDate of Game: ' +str(game_date))

                    self.pushButton.hide()

        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()

            sys.exit(app.exec_())

    def RatingScreen():
        class Ui_MainWindow(QtWidgets.QWidget):
            def setupUi(self, MainWindow):
                MainWindow.resize(422, 255)
                self.centralwidget = QtWidgets.QWidget(MainWindow)

                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(115, 40, 201, 111))

                self.label.setText("")

                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

            def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("RATING CALCULATION", "RATING CALCULATION"))

                rating1, done1 = QtWidgets.QInputDialog.getInt(
                    self, 'Your Rating', 'Enter your rating: ')

                rating2, done2 = QtWidgets.QInputDialog.getInt(
                    self, 'Opponent Rating', "Enter your opponent's rating: ")

                gamescore = ['1', '0', '0.5']
                gamescore, done3 = QtWidgets.QInputDialog.getItem(
                    self, 'Game Point', 'Result of the Game', gamescore)
                gamescore = float(gamescore)

                expected_score = 1 / (1 + (10**((rating2 - rating1) / 400)))
                print(expected_score)
                result_calc = rating1 + (20 * (gamescore - expected_score))
                print(result_calc)
                if result_calc < 0:
                    new_rating = rating2 - result_calc
                else:
                    new_rating = result_calc

                if done1 and done2 and done3:
                    # Showing confirmation message along with information provided by user
                    self.label.setText('Information stored Successfully\nYour Rating: '
                                       + str(rating1) + "\nYour opponent's Rating: " + str(rating2) +
                                       '\n' + 'Your new Rating is: '
                                       + str(new_rating))

                    self.pushButton.hide()

        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()

            sys.exit(app.exec_())


    def HELPscreen():
        class App(QWidget):
            def __init__(self):
                super().__init__()
                self.title = 'Explanation of Features'
                self.left = 10
                self.top = 10
                self.width = 200
                self.height = 200
                self.initUI()

                self.setLayout(qtw.QVBoxLayout())
                my_label = qtw.QLabel(
                    "The is the Chess Board where you can complete your chess analysis or play against the Chess AI.")
                label2 = qtw.QLabel(
                    "The Notation log is where your moves will be recorded and you can perform your own analysis.")
                label3 = qtw.QLabel("The SAVE button will save the current game and recordings in the Notation log.")
                label4 = qtw.QLabel(
                    "The NEW button will open a new Board and Notation log, remember to save your previous one.")
                label5 = qtw.QLabel(
                    "The ENGINE button allows you to modify the actions of the Chess Engine or Chess AI.")
                label6 = qtw.QLabel("The COLOUR THEMES button allows you to modify the colours of the Chess Board.")
                label7 = qtw.QLabel("Those are all the current functioning features of ChessBasics")

                self.layout().addWidget(my_label)
                self.layout().addWidget(label2)
                self.layout().addWidget(label3)
                self.layout().addWidget(label4)
                self.layout().addWidget(label5)
                self.layout().addWidget(label6)
                self.layout().addWidget(label7)
                self.move(450, 325)
                self.show()

            def initUI(self):
                self.setWindowTitle(self.title)
                self.setGeometry(self.left, self.top, self.width, self.height)
                self.show()

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            ex = App()
            sys.exit(app.exec_())


    moveLogFont = p.font.SysFont("Arial", 14, False, False)

    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #notifies when a move is made in order to generate a new set of Legal moves
    animate = False #notifies when we should animate a move
    loadImages()
    highlight = ()
    sqSelected = () #in the event that no square is selected, however will keep track of the last click of the user
    playerClicks = [] #keep track of the square that the player clicks
    gameOver = False
    playerOne = True  #if a human is playing white, then it will be true. (if AI then False)
    playerTwo = True  #same as above but for black
    thinkingTime = False
    multiProcess = None
    moveUndone = False

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
                p.draw.rect(screen, outline, (self.x - 1, self.y - 1, self.width + 2, self.height + 2), 0)

            p.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = p.font.SysFont('Arial', 20)
                text = font.render(self.text, 1, (0, 0, 0))
                screen.blit(text, (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2)))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

    class themesButton():
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
                p.draw.rect(screen, outline, (self.x - 1, self.y - 1, self.width + 2, self.height + 2), 0)

            p.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = p.font.SysFont('Arial', 15)
                text = font.render(self.text, 1, (0, 0, 0))
                screen.blit(text, (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2)))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True


    def redrawWindow():
        screen.fill(p.Color("white"))
        AIwhitebutton.draw(screen, (0, 0, 0))
        AIblackbutton.draw(screen, (0, 0, 0))
        freeAnalysebutton.draw(screen, (0, 0, 0))

        RATINGbutton.draw(screen, (0, 0, 0))
        SAVEbutton.draw(screen, (0, 0, 0))
        NEWbutton.draw(screen, (0, 0, 0))
        HELPbutton.draw(screen, (0, 0, 0))

        greybutton.draw(screen, (0, 0, 0))
        white_pinkbutton.draw(screen, (0, 0, 0))
        light_darkbutton.draw(screen, (0, 0, 0))
        light_brownbutton.draw(screen, (0, 0, 0))
        grey_light_darkbutton.draw(screen, (0, 0, 0))
        bluebutton.draw(screen, (0, 0, 0))

    running = True
    AIwhitebutton = button((224, 224, 224), 521, 7, 225, 50, 'Play CHESS AI as White')
    AIblackbutton = button((224, 224, 224), 756, 7, 225, 50, 'Play CHESS AI as Black')
    freeAnalysebutton = button((224, 224, 224), 991, 7, 200, 50, 'Free Play' )

    SAVEbutton = button((204, 229, 255), 25, 550, 100, 50, 'SAVE')
    NEWbutton = button((204, 229, 255), 150, 550, 100, 50, 'NEW')
    HELPbutton = button((204, 229, 255), 270, 550, 100, 50, 'HELP')
    RATINGbutton = button((204, 229, 255), 390, 550, 100, 50, 'RATINGS')

    greybutton = themesButton((227, 231, 255), 545, 530, 175, 40, 'CLOUDY GREY')
    white_pinkbutton = themesButton((227, 231, 255), 545, 575, 175, 40, 'WHITE/PINK')
    light_darkbutton = themesButton((227, 231, 255), 770, 530, 175, 40, 'LIGHT/DARK')
    light_brownbutton = themesButton((227, 231, 255), 770, 575, 175, 40, 'CREAM/BROWN')
    grey_light_darkbutton = themesButton((227, 231, 255), 985, 530, 175, 40, 'LIGHT/DARK GREY')
    bluebutton = themesButton((227, 231, 255), 985, 575, 175, 40, 'LIGHT/DARK BLUE')

    while running:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                    running = False
            #mouse presses to enbale different functions for the program
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver:
                    location = p.mouse.get_pos() #(x, y) location of mouse
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE

                    if sqSelected == (row, col) or col >= 8 or row >= 8:  #in the event that the user clicks the square twice or mouse log/buttons
                        sqSelected = ()  #clears the players click as it will likely be an undo action
                        playerClicks = []  #officially clears the player's click
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected) #changes both clicks
                    if len(playerClicks) == 2 and humanTurn: #after the 2nd click
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = () #resets the user clicks so that they can make another move
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected] #storing the second click

            #key presses to enable different functions in the program
            elif e.type == p.KEYDOWN:
                if e.key == p.K_LEFT: #when the left arrow is pressed, the move most recerntly played will go back.
                    gs.undoMove()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = True
                    animate = False
                    gameOver = False
                    if thinkingTime:
                        multiProcess.terminate()
                        thinkingTime = False
                        moveUndone = True

                if e.key == p.K_r:  #resets the board
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    highlight = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    if thinkingTime:
                        multiProcess.terminate()
                        thinkingTime = False
                    moveUndone = True

        click = p.mouse.get_pressed()
        redrawWindow()
        for e in p.event.get():
            pos = p.mouse.get_pos()
            if click[0] == 1:
                if AIwhitebutton.isOver(pos):
                    print('Clicked')

                if AIblackbutton.isOver(pos):
                    print('Clicked')

            if e.type == p.MOUSEBUTTONDOWN:
                if AIwhitebutton.isOver(pos):
                    print('Clicked')
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    highlight = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    AIwhitebutton.color = (224, 224, 224)
                    AIblackbutton.color = (128, 128, 128)
                    freeAnalysebutton.color = (128, 128, 128)
                    playerTwo = False
                    playerOne  =True

                if AIblackbutton.isOver(pos):
                    print('Clicked')
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    highlight = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    AIblackbutton.color = (224, 224, 224)
                    AIwhitebutton.color = (128, 128, 128)
                    freeAnalysebutton.color = (128, 128, 128)
                    playerTwo = True
                    playerOne = False

                if freeAnalysebutton.isOver(pos):
                    print('Clicked')
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    highlight = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    freeAnalysebutton.color = (224, 224, 224)
                    AIblackbutton.color = (128, 128, 128)
                    AIwhitebutton.color = (128, 128, 128)
                    playerTwo = True
                    playerOne = True

                if RATINGbutton.isOver(pos):
                    print("Clicked")
                    RatingScreen()

                if SAVEbutton.isOver(pos):
                    print('clicked')
                    SaveScreen()

                if NEWbutton.isOver(pos):
                    print('clicked')
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    highlight = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    if thinkingTime:
                        multiProcess.terminate()
                        thinkingTime = False
                    moveUndone = True

                if HELPbutton.isOver(pos):
                    print('clicked')
                    HELPscreen()

                if greybutton.isOver(pos):
                    global board_colour
                    print('clicked')
                    board_colour = (GREY_LIGHT, GREY_DARK)

                if white_pinkbutton.isOver(pos):
                    print('clicked')
                    board_colour = (WHITE, RED_CHECK)

                if light_darkbutton.isOver(pos):
                    print('clicked')
                    board_colour = (LIGHT, DARK)

                if light_brownbutton.isOver(pos):
                    print('clicked')
                    board_colour = (LICHESS_LIGHT, LICHESS_DARK)

                if grey_light_darkbutton.isOver(pos):
                    print('clicked')
                    board_colour = (LICHESS_GREY_LIGHT, LICHESS_GREY_DARK)

                if bluebutton.isOver(pos):
                    print('clicked')
                    board_colour = (BLUE_LIGHT, BLUE_DARK)



            elif e.type == p.MOUSEMOTION:
                if SAVEbutton.isOver(pos):
                    SAVEbutton.color = (153, 204, 255)
                else:
                    SAVEbutton.color = (204, 229, 255)

                if RATINGbutton.isOver(pos):
                    RATINGbutton.color = (153, 204, 255)
                else:
                    RATINGbutton.color = (204, 229, 255)

                if NEWbutton.isOver(pos):
                    NEWbutton.color = (153, 204, 255)
                else:
                    NEWbutton.color = (204, 229, 255)

                if HELPbutton.isOver(pos):
                    HELPbutton.color = (153, 204, 255)
                else:
                    HELPbutton.color = (204, 229, 255)

                if greybutton.isOver(pos):
                    greybutton.color = (189, 198, 255)
                else:
                    greybutton.color = (227, 231, 255)

                if white_pinkbutton.isOver(pos):
                    white_pinkbutton.color = (189, 198, 255)
                else:
                    white_pinkbutton.color = (227, 231, 255)

                if light_brownbutton.isOver(pos):
                    light_brownbutton.color = (189, 198, 255)
                else:
                    light_brownbutton.color = (227, 231, 255)

                if grey_light_darkbutton.isOver(pos):
                    grey_light_darkbutton.color = (189, 198, 255)
                else:
                    grey_light_darkbutton.color = (227, 231, 255)

                if bluebutton.isOver(pos):
                    bluebutton.color = (189, 198, 255)
                else:
                    bluebutton.color = (227, 231, 255)

                if light_darkbutton.isOver(pos):
                    light_darkbutton.color = (189, 198, 255)
                else:
                    light_darkbutton.color = (227, 231, 255)


        #AI logic
        if not gameOver and not humanTurn and not moveUndone:
            if not thinkingTime:
                thinkingTime = True
                print("Evaluating moves...")
                returnQueue = Queue() #container for potential values that change and passing data
                multiProcess = Process(target = Chess_AI.BestMove, args =(gs, validMoves, returnQueue))
                multiProcess.start() #begins the function without delaying other functions

            if not multiProcess.is_alive():
                print("Found a move...")
                AImove = returnQueue.get()
                if AImove is None:
                    AImove = Chess_AI.BestMove(validMoves)
                    #AImove = Chess_AI.RandomMove(validMoves)
                gs.makeMove(AImove)
                moveMade = True
                animate = True
                thinkingTime = False

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, validMoves, sqSelected, moveLogFont, highlight)

        if gs.checkmate or gs.stalemate:
            gameOver = True
            drawEndGameText(screen, 'Stalemate' if gs.stalemate else 'Black wins by Checkmate' if gs.whiteToMove else 'White wins by Checkmate')

        clock.tick(MAX_FPS)
        p.display.flip()

"""
Responsible for all the graphics within a current game state   
"""

def drawGameState(screen, gs, validMoves, sqSelected, moveLogFont, highlight):
    drawBoard(screen)# draws squares on the board
    highlightSquares(screen, gs, validMoves, sqSelected, highlight)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares
    drawMoveLog(screen, gs, moveLogFont)

"""
Highlight square selected and move for piece selected
"""
def highlightSquares(screen, gs, validMoves, sqSelected, highlight):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            #highlight selected square
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill((p.Color)('blue'))
            screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
            #highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))
    if p.K_1:
        if highlight != ():
            h = p.Surface((SQ_SIZE, SQ_SIZE))
            h.fill((p.Color)('pink'))
            screen.blit(h, (c * SQ_SIZE, r * SQ_SIZE))

"""
Draws the Move log
"""
def drawMoveLog(screen, gs, font):
    moveLogRect = p.Rect(WIDTH, 64, MOVE_LOG_PANEL_HEIGHT, MOVE_LOG_PANEL_WIDTH)

    p.draw.rect(screen, p.Color("White"), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = []
    #adding numbers to the different moves
    for i in range(0, len(moveLog), 2):
        moveString = str(i//2 +1) + ". " + str(moveLog[i]) + " "
        if i+1 < len(moveLog): #making sure that black has made a move
            moveString += str(moveLog[i+1]) + "  "
        moveTexts.append(moveString)

    movesPerRow = 8
    padding = 5
    lineSpacing = 2
    textSpace = padding
    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i+j]
        textObject = font.render(text, True, p.Color('Dark Blue'))
        textLocation = moveLogRect.move(padding, textSpace)
        screen.blit(textObject, textLocation)
        textSpace += textObject.get_height() + lineSpacing

'''
Draw the squares on the board - the top left square is always light
'''
def drawBoard(screen):
    global colors
    colors = board_colour
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""
Animating a move
"""
def animateMove(move, screen, board, clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR * frame/frameCount, move.startCol + dC * frame/frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        #erase the piece moves from its ending square
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol * SQ_SIZE, move.endRow * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, endSquare)
        #draw captured piece onto rectangle
        if move.pieceCaptured != '--':
            if move.isEnpassantMove:
                RowEnpassant = move.endRow + 1 if move.pieceCaptured[0] == 'b' else move.endRow - 1
                endSquare = p.Rect(move.endCol * SQ_SIZE, RowEnpassant * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        #draw moving piece
        screen.blit(IMAGES[move.pieceMoved], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)

def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    textObject = font.render(text, 0, p.Color('Gray'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, 0, p.Color('Black'))
    screen.blit(textObject, textLocation.move(2, 2))

if __name__ == "__main__":
    main()

