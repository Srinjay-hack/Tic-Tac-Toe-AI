#Tic Tac Toe game in python

board = [' ' for x in range(10)]

def inLetter(letter, pos):
    board[pos] = letter

def Freespace(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def Win(xc, zx):
    return (xc[7] == zx and xc[8] == zx and xc[9] == zx) or (xc[4] == zx and xc[5] == zx and xc[6] == zx) or(xc[1] == zx and xc[2] == zx and xc[3] == zx) or(xc[1] == zx and xc[4] == zx and xc[7] == zx) or(xc[2] == zx and xc[5] == zx and xc[8] == zx) or(xc[3] == zx and xc[6] == zx and xc[9] == zx) or(xc[1] == zx and xc[5] == zx and xc[9] == zx) or(xc[3] == zx and xc[5] == zx and xc[7] == zx)

def playerMove():
    job = True
    while job:
        step = input('Please select a position to place an \'X\' (1-9): ')
        try:
            step = int(step)
            if step > 0 and step < 10:
                if Freespace(step):
                    job = False
                    inLetter('X', step)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def computerMove():
    combination = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in combination:
            boardCopy = board[:]
            boardCopy[i] = letter
            if Win(boardCopy, letter):
                move = i
                return move

    corners = []
    for i in combination:
        if i in [1,3,7,9]:
            corners.append(i)
            
    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    if 5 in combination:
        move = 5
        return move

    edges = []
    for i in combination:
        if i in [2,4,6,8]:
            edges.append(i)
            
    if len(edges) > 0:
        move = selectRandom(edges)
        
    return move

def selectRandom(lst):
    import random
    ln = len(lst)
    r = random.randrange(0,ln)
    return lst[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(Win(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won this time!')
            break

        if not(Win(board, 'X')):
            move = computerMove()
            if move == 0:
                print('Tie Game!')
            else:
                inLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time!)
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
