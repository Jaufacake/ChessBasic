#This section is responsible for storing all of the information about the current state of the chess game and
#determing legal moves; as well as keep notation (log of moves to enable takebacks etc)

class GameState():
    def __init__(self):

    #board is 8x8 2d list, each element of the list has 2 characters
    #the first character represents the colour of the piece, 'b' or 'w'
    #the second character represents the type of the piece, 'K', 'Q', 'R', 'B', 'N', 'P'.
    #'--' represents an empty space with no piece

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ['--', "--", '--', '--', '--', '--', '--', '--'],
            ['--', "--", '--', '--', '--', '--', '--', '--'],
            ['--', "--", '--', '--', '--', '--', '--', '--'],
            ['--', "--", '--', '--', '--', '--', '--', '--'],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.moveFunctions = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                              'B': self.getBishopMoves,'Q': self.getQueenMoves, 'K': self.getKingMoves}


        self.whiteToMove = True
        self.moveLog = []
        self.whiteKinglocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.potentialEnpassant = ()  #the coordinates where en passant is possible
        self.potentialEnpassantLog = [self.potentialEnpassant]
        self.currentCastlingRight = CastleRights(True, True, True, True)
        self.castleRightsLog = [CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                         self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)]

    '''
    Takes a move and executes it - however will not do this for castling, pawn promotion and en passant
    '''
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #refers back to the Movelog() so that the user can undo their moves at any point/keep track
        self.whiteToMove = not self.whiteToMove #ensures the swap of players to enable correct play
        #updating the king's location if they moved
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow, move.endCol)

        #pawn promotion
        if move.isPawnPromotion:
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + 'Q'

        #enpassant move
        if move.isEnpassantMove:
            self.board[move.startRow][move.endCol] = "--"  #capturing the pawn

        #update enpassant variable
        if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:  #only on 2 square pawn advances
            self.potentialEnpassant = ((move.startRow + move.endRow)//2, move.startCol)
        else:
            self.potentialEnpassant = ()

        #castling
        if move.isCastleMove:
            if move.endCol - move.startCol == 2:  #castling on the kingside
                self.board[move.endRow][move.endCol - 1] = self.board[move.endRow][move.endCol + 1]  #moves the rook
                self.board[move.endRow][move.endCol + 1] = '--' #erase the rook on the start square (bottom corners)
            else:  #castling on the queenside
                self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.endCol - 2]  #moves the rook
                self.board[move.endRow][move.endCol - 2] = '--'

        self.potentialEnpassantLog.append(self.potentialEnpassant)

        #update castling rights - whenever it is a king or a rook move
        self.updateCastleRights(move)
        self.castleRightsLog.append(CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                                 self.currentCastlingRight.wqs, self.currentCastlingRight.bqs))

    """
    creating a function that allows the user to undo the last move made
    """

    def undoMove(self):
        if len(self.moveLog) != 0: #this ensure that there is a move that can be undone
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #the turn changes
            # updating the king's location if they moved
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow, move.startCol)
            #undo enpassant
            if move.isEnpassantMove:
                self.board[move.endRow][move.endCol] = '--'  #leaving landing square blank
                self.board[move.startRow][move.endCol] = move.pieceCaptured

            self.potentialEnpassantLog.pop()
            self.potentialEnpassant = self.potentialEnpassantLog[-1]

            #undo castling rights
            self.castleRightsLog.pop()  #get rid of the new castle rights from the move we are doing
            newRights = self.castleRightsLog[-1]
            self.currentCastlingRight = CastleRights(newRights.wks, newRights.bks, newRights.wqs, newRights.bqs)

            #undo castle move
            if move.isCastleMove:
                if move.endCol - move.startCol == 2:  #kingside caslte move
                    self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.endCol - 1]
                    self.board[move.endRow][move.endCol - 1] = '--'
                else:  #queenside castle move
                    self.board[move.endRow][move.endCol - 2] = self.board[move.endRow][move.endCol + 1]
                    self.board[move.endRow][move.endCol + 1] = '--'

            self.checkmate = False;
            self.stalemate = False;

    """
    update castle rights given the move
    """
    def updateCastleRights(self, move):
        if move.pieceMoved == 'wK':
            self.currentCastlingRight.wks = False
            self.currentCastlingRight.wqs = False
        elif move.pieceMoved == 'bK':
            self.currentCastlingRight.bks = False
            self.currentCastlingRight.bqs = False
        elif move.pieceMoved == 'wR':
            if move.startRow == 7:
                if move.startCol == 0:  #left rook
                    self.currentCastlingRight.wqs = False
                elif move.startCol == 7:  #right rook
                    self.currentCastlingRight.wks = False
        elif move.pieceMoved == 'bR':
            if move.startRow == 0:
                if move.startCol == 0:  #left rook
                    self.currentCastlingRight.bqs = False
                elif move.startCol == 7:  #right rook
                    self.currentCastlingRight.bks = False

        if move.pieceCaptured == 'wR':
            if move.endRow == 7:
                if move.endCol == 0:
                    self.currentCastlingRight.wqs = False
                elif move.endCol == 7:
                    self.currentCastlingRight.wks = False
        elif move.pieceCaptured == 'bR':
            if move.endRow == 0:
                if move.endCol == 0:
                    self.currentCastlingRight.bqs = False
                elif move.endCol == 7:
                    self.currentCastlingRight.bks = False

    """
    All moves considering checks
    """
    def getValidMoves(self):
        tempPotentialEnpassant = self.potentialEnpassant
        tempCastleRights = CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                        self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)
        #generate all possible moves
        moves = self.getAllPossibleMoves()

        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        if len(moves) == 0: #either checkmate or stalemate
            if self.inCheck():
                self.checkmate = True
            else:
                self.stalemate = True

        if self.whiteToMove:
            self.getCastleMoves(self.whiteKinglocation[0], self.whiteKinglocation[1], moves)
        else:
            self.getCastleMoves(self.blackKingLocation[0], self.blackKingLocation[1], moves)
        self.potentialEnpassant = tempPotentialEnpassant
        self.currentCastlingRight = tempCastleRights
        return moves

    """
    Determine if the current player is in check
    """
    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKinglocation[0], self.whiteKinglocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    """
    Determine where the enemy can attack the square r, c
    """
    def squareUnderAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove  #switch turns
        oppMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove  #switch turns back
        for move in oppMoves:
            if move.endRow == r and move.endCol == c:  #square is under attack
                return True
        return False

    """
    All moves without considering checks
    """
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #8 rows and 8 columns
            for c in range(len(self.board[r])): #this is for the length of the current row that we are looking at
               colourTurn = self.board[r][c][0]
               if (colourTurn == 'w' and self.whiteToMove) or (colourTurn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)  #calls the appropriate move functions for the specific piece
        return moves


    '''
    Get all the pawn moves for the pawn location and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove: #white pawn moves
            if self.board[r-1][c] == "--": #'r-1' as we are going up the board, hence decreasing rows : showing a 1 square pawn advance
                #if not piecePinned or pinDirection == (-1, 0):
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--": #for a pawn advancing 2 squares
                    moves.append(Move((r, c), (r-2, c), self.board))

            #CAPTURES
            if c-1 >= 0: #avoid columns going into the negatives and showing errors - CAPTURES TO THE LEFT
                if self.board[r-1][c-1][0] == 'b': #shows that there is an opposing piece on that square for capturing
                    moves.append(Move((r, c), (r-1, c-1), self.board))
                elif(r-1, c-1) == self.potentialEnpassant:
                    moves.append(Move((r, c), (r-1, c-1), self.board, isEnpassantMove = True))
            if c+1 <= 7: #CAPTURES TO THE RIGHT - last column for capturing (8x8 DIMENSION)
                if self.board[r-1][c+1][0] == 'b': #shows that there is an opposing piece on that square for capturing
                    moves.append(Move((r, c), (r-1, c+1), self.board))
                elif (r-1, c+1) == self.potentialEnpassant:
                    moves.append(Move((r, c), (r-1, c+1), self.board, isEnpassantMove = True))

        else: #black pawn moves
            if self.board[r+1][c] == "--": #for a pawn advancing one square, as the rows are 'increasing' from White's POV
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--": #for a pawn advancing 2 squares
                    moves.append(Move((r, c), (r+2, c), self.board))

            #CAPTURES
            if c-1 >= 0: # CAPTURES TO THE LEFT
                if self.board[r+1][c-1][0] == 'w':
                    #if not piecePinned or pinDirection == (1, -1):
                    moves.append(Move((r, c), (r+1, c-1), self.board))
                elif (r+1, c-1) == self.potentialEnpassant:
                    moves.append(Move((r, c), (r+1, c-1), self.board, isEnpassantMove = True))

            if c+1 <= 7: #CAPTURES TO THE RIGHT
                if self.board[r+1][c+1][0] == 'w':
                    #if not piecePinned or pinDirection == (1, 1):
                    moves.append(Move((r, c), (r+1, c+1), self.board))
                elif (r+1, c+1) == self.potentialEnpassant:
                    moves.append(Move((r, c), (r+1, c+1), self.board, isEnpassantMove = True))

    '''
    Get all the rook moves for the rook location and add these moves to the list
    '''
    def getRookMoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))  #up, down, left and right directions
        enemyColour = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: #check the square ON the board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--": #whether the square is empty
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour: #enemy piece is legal to capture
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else:        #illegal to take a friendly-piece
                        break
                else:            #whether the square is off the board
                    break

    '''
    Get all the knight moves for the knight location and add these moves to the list
    '''
    def getKnightMoves(self, r, c, moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColour = "w" if self.whiteToMove else "b"
        for m in knightMoves:
            endRow = r + m[0]
            endCol = c + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                #if not piecePinned:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColour: #checking it is an empty/enemy-occupied square (not one of its own pieces)
                    moves.append(Move((r, c), (endRow, endCol), self.board))

    '''
    Get all the bishop moves for the bishop location and add these moves to the list
    '''
    def getBishopMoves(self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  #the 4 diagonals the bishop can potentially move to
        enemyColour = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8): #maximum moves of a bishop on a diagonal is 7
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else:        #illegal to take a friendly-piece
                        break
                else:            #whether the square is off the board
                    break

    '''
    Get all the Queen moves for the Queen location and add these moves to the list
    '''
    #the queen has the greatest flexibility of movement. It is combined by the rook and bishop 's movements
    def getQueenMoves(self, r, c, moves):
        self.getRookMoves(r, c, moves)
        self.getBishopMoves(r, c, moves)

    '''
    Get all the king moves for the king location and add these moves to the list
    '''
    def getKingMoves(self, r, c, moves):
        kingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        allyColour = "w" if self.whiteToMove else "b"
        for i in range(8):
            endRow = r + kingMoves[i][0]
            endCol = c + kingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColour:  #check that it is empty/enemy-occupied (not one of its own pieces)
                    moves.append(Move((r, c), (endRow, endCol), self.board))

    """
    Generate all valid castle moves for the king at (r, c) and add them to the list of moves
    """
    def getCastleMoves(self, r, c, moves):
        if self.squareUnderAttack(r, c):
            return  #you can't caslte whislt you are in check
        if (self.whiteToMove and self.currentCastlingRight.wks) or (not self.whiteToMove and self.currentCastlingRight.bks):
            self.getKingsideCastleMoves(r, c, moves)
        if (self.whiteToMove and self.currentCastlingRight.wqs) or (not self.whiteToMove and self.currentCastlingRight.bqs):
            self.getQueensideCastleMoves(r, c, moves)

    def getKingsideCastleMoves(self, r, c, moves):
        if self.board[r][c+1] == '--' and self.board[r][c+2] == '--' and \
         not self.squareUnderAttack(r, c+1) and not self.squareUnderAttack(r, c+2):
            moves.append(Move((r, c), (r, c+2), self.board, isCastleMove = True))

    def getQueensideCastleMoves(self, r, c, moves):
        if self.board[r][c-1] == '--' and self.board[r][c-2] == '--' and self.board[r][c-3] == '--' and \
         not self.squareUnderAttack(r, c-1) and not self.squareUnderAttack(r, c-2):
            moves.append(Move((r, c), (r, c-2), self.board, isCastleMove = True))

class CastleRights():
    def __init__(self, wks, bks, wqs, bqs):
        self.wks = wks
        self.bks = bks
        self.wqs = wqs
        self.bqs = bqs

class Move():
    #maps the keys to values
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board, isEnpassantMove=False, isCastleMove=False):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.castle = isCastleMove
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        #pawn promotion
        self.isPawnPromotion = (self.pieceMoved == 'wp' and self.endRow == 0) or (self.pieceMoved == 'bp' and self.endRow == 7)
        #en passant
        self.isEnpassantMove = isEnpassantMove
        if self.isEnpassantMove:
            self.pieceCaptured = 'bp' if self.pieceMoved == 'wp' else 'wp'
        #castle move
        self.isCastleMove = isCastleMove

        self.isCapture = self.pieceCaptured != '--'
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    """
    Overriding the equals method
    """
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        #add to make it real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKinglocation[0], self.whiteKinglocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    #overriding the str() function
    def __str__(self):
        if self.castle:
            return "O-O" if self.endCol == 6 else "O-O-O"
            #"O-O" kingside castling notation
            #"O-O-O" #queenside castling notation

        endSquare = self.getRankFile(self.endRow, self.endCol)
        if self.pieceMoved[1] == 'p':
            if self.isCapture:
                return self.colsToFiles[self.startCol] + "x" + endSquare
            else:
                return endSquare

        #add pawn promotions and distinguish two pieces able to move to the same square and check/checkmate symbols

        #other piece move notations
        moveString = self.pieceMoved[1]
        if self.isCapture:
            moveString += 'x'
        #elif self.inCheck:
        #    return moveString + endSquare + "+"
        return moveString + endSquare
