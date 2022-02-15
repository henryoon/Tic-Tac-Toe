from curses.ascii import isdigit


board = ([None, None, None], [None, None, None], [None, None, None])


def showBoard():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                board[i][j] = "-"
            elif board[i][j] is True:
                board[i][j] = "O"
            elif board[i][j] is False:
                board[i][j] = "X"
            print(board[i][j], end="\t")
        print()



def py1():
    global board
    while True:
        po = input("위치를 입력하시오: ")   # a1
        # if len(po) != 2:
        #     print("다시 입력하시오.")
        #     return po
        # elif isdigit(po[1]) is False:
        #     print("숫자를 다시 입력하시오.")
        #     return po
        # elif po[1] != "1" or po[1] != "2" or po[1] != "3":
        #     print("숫자는 1에서 3까지 입력하시오.")
        #     return po 
        row = str(po[0])  # a
        col = int(po[1])  # 1
        col = col - 1
        if row == 'A' or row == 'a':
            row = 0
            break
        elif row == 'B' or row == 'b':
            row = 1
            break
        elif row == 'C' or row == 'c':
            row = 2
            break
        # else:
        #     print("영어(열)을 다시 입력하시오.")
        #     return po

    board[row][col] = True


def py2():
    global board
    while True:
        po = input("위치를 입력하시오: ")   # a1
        row = str(po[0])  # a
        col = int(po[1])  # 1
        col = col - 1
        if row == 'A' or row == 'a':
            row = 0
            break
        elif row == 'B' or row == 'b':
            row = 1
            break
        elif row == 'C' or row == 'c':
            row = 2
            break
        # elif col < 0 or col > 2:
        #     print("행(숫자)를 다시 입력하시오. ")
        #     return po
        # else:
        #     print("열(영문)을 다시 입력하시오.")
        #     return po


    board[row][col] = False


# def confirm():
#     py1()
#     if len(po) 


def winner():
    global board
    # print("-------------------")
    # print(board[0][0], board[0][1], board[0][2])
    # print(board[1][0], board[1][1], board[1][2])
    # print(board[2][0], board[2][1], board[2][2])
    # print("-------------------")

    if board[0][0] == board[0][1] == board[0][2] == "O":
        print("****************-player 1 wins****************")
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("****************-player 1 wins****************")
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("****************-player 1 wins****************")
    elif board[0][0] == board[0][1] == board[0][2] == "X":
        print("****************-player 2 wins****************")
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("****************-player 2 wins****************")
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("****************-player 2 wins****************")
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("****************-player 1 wins****************")
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print("****************-player 1 wins****************")
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print("****************-player 1 wins****************")
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        print("****************-player 2 wins****************")
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        print("****************-player 2 wins****************")
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print("****************-player 2 wins****************")
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("****************-player 1 wins****************")
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print("****************-player 2 wins****************")

    



if __name__ == '__main__':
    showBoard()
    while True:
        py1()
        showBoard()
        winner()
        py2()
        showBoard()
        winner()
