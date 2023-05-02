#this module will handle the literal chess engine for the analysis

import random

#this shows how much each piece is worth
pieceValue = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1}


#this is a 2D map that represents the best places for the knight with a 1-4 scale: 4 being the best place, 1 being the worst
knightValue = [[1, 1, 1, 1, 1, 1, 1, 1],
               [1, 2, 2, 2, 2, 2, 2, 1],
               [1, 2, 5, 3, 3, 5, 2, 1],
               [1, 3, 3, 4, 4, 3, 3, 1],
               [1, 3, 3, 4, 4, 3, 3, 1],
               [1, 2, 5, 3, 3, 5, 2, 1],
               [1, 2, 2, 2, 2, 2, 2, 1],
               [1, 1, 1, 1, 1, 1, 1, 1]]

queenValue = [[1, 1, 1, 3, 1, 1, 1, 1],
              [1, 2, 2, 3, 2, 2, 2, 1],
              [1, 4, 3, 3, 3, 4, 2, 1],
              [1, 2, 3, 3, 4, 3, 2, 1],
              [1, 2, 3, 3, 4, 3, 2, 1],
              [1, 4, 3, 3, 3, 4, 2, 1],
              [1, 2, 2, 3, 2, 2, 2, 1],
              [1, 1, 1, 3, 1, 1, 1, 1]]

rookValue = [[4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4],
             [1, 1, 3, 3, 3, 3, 1, 1],
             [1, 2, 3, 4, 4, 3, 2, 1],
             [1, 2, 3, 4, 4, 3, 2, 1],
             [1, 1, 3, 3, 3, 3, 1, 1],
             [4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4]]

whitePawnValue = [[7, 7, 7, 7, 7, 7, 7, 7],
                  [7, 7, 7, 7, 7, 7, 7, 7],
                  [4, 4, 3, 6, 6, 5, 3, 4],
                  [1, 2, 3, 5, 5, 3, 2, 1],
                  [2, 2, 4, 5, 5, 4, 2, 2],
                  [2, 2, 2, 2, 2, 1, 2, 2],
                  [1, 1, 1, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

blackPawnValue = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 1, 1, 1],
                  [2, 2, 2, 2, 2, 1, 2, 2],
                  [2, 2, 4, 5, 5, 4, 2, 2],
                  [1, 2, 3, 5, 5, 3, 2, 1],
                  [4, 4, 3, 6, 6, 5, 3, 4],
                  [7, 7, 7, 7, 7, 7, 7, 7],
                  [7, 7, 7, 7, 7, 7, 7, 7]]

bishopValue = [[4, 3, 2, 1, 1, 2, 3, 4],
               [3, 4, 3, 2, 2, 3, 4, 3],
               [2, 3, 4, 3, 3, 4, 3, 2],
               [1, 2, 3, 4, 4, 3, 2, 1],
               [1, 2, 3, 4, 4, 3, 2, 1],
               [2, 3, 4, 3, 3, 4, 3, 2],
               [3, 4, 3, 2, 2, 3, 4, 3],
               [4, 3, 2, 1, 1, 2, 3, 4]]


#dictionary evaluating the 2D map for each piece
piecePositionValues = {"N": knightValue, "Q": queenValue, "B": bishopValue,
                       "wp": whitePawnValue, "bp": blackPawnValue, "R": rookValue}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 4

"""
Picks a random move to play
"""
def RandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) -1)]

"""
Helper method to make first recursive call
"""
def BestMove(gs, validMoves, returnQueue):
    global nextMove, counter
    nextMove = None
    counter = 0
    MoveNegaMaxAlphaBeta(gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    random.shuffle(validMoves)
    print("Number of Game States considered: ", counter)
    returnQueue.put(nextMove)


#calling this method recursively
def MoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove
    if depth == 0:
        return scoreBoard(gs.board)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = MoveMinMax(gs, nextMoves, depth - 1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = MoveMinMax(gs, nextMoves, depth - 1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore

def MoveNegaMax(gs, validMoves, depth, turnMultiplier):
    global nextMove, counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -MoveNegaMax(gs, nextMoves, depth - 1, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
    return maxScore

"""
Alpha - Beta pruning implementations
"""
def MoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove, counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -MoveNegaMaxAlphaBeta(gs, nextMoves, depth - 1, -alpha, -beta, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
                print(move, score)
        gs.undoMove()
        if maxScore > alpha: #pruning occurs
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore



"""
Engine Evaluation: A positive score = for white, a negative score = good for black
"""
def scoreBoard(gs):
    if gs.checkmate:
        if gs.whiteToMove:
            return -CHECKMATE #Black wins
        else:
            return CHECKMATE #White wins
    elif gs.stalemate:
        return STALEMATE #neither side wins

    score = 0
    #using the range and len functions give a precise number between 0-7 of the row and col so that a direct
    #comparison can be made rather than a hypothetical square
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != "--":
                piecePositionValue = 0
                #implementation of positional evaluation
                if square[1] != "K":
                    #fetches the positional score from the dictionary (1-4 scaling)
                    if square[1] == "p":
                        piecePositionValue = piecePositionValues[square][row][col]
                    else:
                        piecePositionValue = piecePositionValues[square[1]][row][col]

                if square[0] == 'w':
                    score += (pieceValue[square[1]] * 0.01) + (piecePositionValue * 0.0001)
                elif square[0] == 'b':
                    score -= (pieceValue[square[1]] * 0.01) + (piecePositionValue * 0.0001)
    return score

