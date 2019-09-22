import random
#dictionary containing keys of letters and values that represent which row or column
meanings = {"B" : "bottom", "M" : "middle", "T" : "top", "L": "left", "R" : "right" }

def index2location(i):  # 0 <= i <= 8
    if type(i) != type(1):
        raise TypeError
    if not 0 <= i <= 8:
        raise ValueError
    row = i // 3
    col = i % 3
    return (row, col)

def location2index(where):  # where is a tuple (row, col)
    if type(where) != type((1, 2)):
        raise TypeError
    if len(where) != 2:
        raise TypeError
    if not 0 <= where[0] <= 2:
        raise ValueError
    if not 0 <= where[1] <= 2:
        raise ValueError
    row = where[0]
    col = where[1]
    retval = row * 3 + col
    return retval
        

def newTicTac():
    xs = []
    os = []
    empties = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return (xs, os, empties)

def makeMove(xory, row, col, xs, os, empties):
    if xory.upper() != 'X' and xory.upper() != 'O':
        raise ValueError
    if not 0 <= row <= 2:
        raise ValueError
    if not 0 <= col <= 2:
        raise ValueError
    i = location2index((row, col))
    if i in empties:
        if xory == 'X':
            xs.append(i)
        elif xory == 'O':
            os.append(i)
        empties.remove(i)
    else:
        raise ValueError

def print_board(xs, os, empties):
    print('   L  M  R')
    print(' ---------')
    print('T|', end='')
    for i in range(0, 9): #start from 0 and end at 8
        if i in xs:
            next = 'X'
        elif i in os:
            next = 'O'
        else:
            next = ' '
        if i == 2: #print a bar, and then a horizontal separater
            print(next, '|')
            print(' ---------') #this automatically has carriage return
            print('M|', end='')
        elif i == 5:
            print(next, '|')
            print(' ---------') #carriage return at end for new row
            print('B|', end='')
        elif i == 8:
            print(next, '|')
            print(' ---------')
        else:           
            print(next, '|', end='')


def won(xos):  # xos is xs to check for x win, ys to check for y win
    if len(xos) < 3:
        return False
    if 0 in xos and 1 in xos and 2 in xos:
        return True
    if 3 in xos and 4 in xos and 5 in xos:
        return True
    if 6 in xos and 7 in xos and 8 in xos:
        return True
    if 0 in xos and 3 in xos and 6 in xos:
        return True
    if 1 in xos and 4 in xos and 7 in xos:
        return True
    if 2 in xos and 5 in xos and 8 in xos:
        return True
    if 0 in xos and 4 in xos and 8 in xos:
        return True
    if 2 in xos and 4 in xos and 6 in xos:
        return True
    return False

def winnable(xs, os, empties):
    for x in empties: #check all empties for possible win
        xtest = xs[:] #perfect copy of whatever is in xs currently
        xtest.append(x) #append to test
        if won(xtest):
            return x
    for x in empties: #if nothing, look for a block
        otest = os[:] #make perfect copy of whatever is in os currently
        otest.append(x) #append to test
        if won(otest):
            return x
    if 4 in spaces: #if no chance of block, no chance to win, put center if empty
        return 4
    return random.choice(empties) #otherwise, just make random move

def isValid(xs, os, spaces):
    retval = True
    if not (len(xs) == len(os) or len(xs) == len(os) + 1):
        retval = False
    if won(xs) and won(os):
        retval = False
    return retval


if __name__ == "__main__":
    xs, os, spaces = newTicTac()
    print_board(xs, os, spaces)
    moves_made = 0
    done = False
    while not done:
        where = winnable(xs, os, spaces)
        row, col = index2location(where)
        makeMove('X', row, col, xs, os, spaces)
        print_board(xs, os, spaces)
        if won(xs):
            done = True
            print("Computer wins!") #after computer makes move, check for win condition
        elif len(spaces) == 0: #no more empty, can't play anymore (tie game)
            done = True
            print("It's a tie!")
        else: #else, continue playing
            r = input('Which row for your O (T, M, or B):')
            r = r.upper()
            if r == 'T':
                row = 0
                print("meaning is...", meanings["T"])
            elif r == 'M':
                print("meaning is...", meanings["M"])
                row = 1
            elif r == 'B':
                print("meaning is...", meanings["B"])
                row = 2
            else:
                print("Learn to read directions")
                print("You lose")
                done = True
            c = input('Which column for your O (L, M, or R):')
            c = c.upper()
            if c == 'L':
                col = 0
                print("meaning is...", meanings["L"])
            elif c == 'M':
                col = 1
                print("meaning is...", meanings["M"])
            elif c == 'R':
                col = 2
                print("meaning is...", meanings["R"])
            else:
                print("Learn to read directions")
                print("You lose")
                done = True
            if not done:
                makeMove('O', row, col, xs, os, spaces)
                if won(os): #after human makes a move, check for win condition
                    done = True
                    print("Human wins!") 
                    print_board(xs, os, spaces)
                else:
                    print_board(xs, os, spaces)









