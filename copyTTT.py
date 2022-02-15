inputDict= {
    1 : " ", 2 : " ", 3 : " ",
    4 : " ", 5 : " ", 6 : " ",
    7 : " ", 8 : " ", 9 : " ",
}

def checkDuplicate(position):
    duplicateCheck = False
    if inputDict[position] != " ":
        duplicateCheck = True

    return duplicateCheck

def setData(position,value):
    inputDict[position] = value


def printBoard():
    print("{}|{}|{}".format(inputDict[1],inputDict[2],inputDict[3]))
    print("------")
    print("{}|{}|{}".format(inputDict[4],inputDict[5],inputDict[6]))
    print("------")
    print("{}|{}|{}".format(inputDict[7],inputDict[8],inputDict[9]))


def confirmVictory(turn):
    if inputDict[1] == turn and inputDict[2]  == turn and inputDict[3] == turn:
         return True
    elif inputDict[1] == turn and inputDict[4]  == turn and inputDict[7] == turn:
         return True
    elif inputDict[1] == turn and inputDict[5]  == turn and inputDict[9] == turn:
         return True
    elif inputDict[4] == turn and inputDict[5]  == turn and inputDict[6] == turn:
         return True
    elif inputDict[7] == turn and inputDict[8]  == turn and inputDict[9] == turn:
         return True
    elif inputDict[2] == turn and inputDict[5]  == turn and inputDict[8] == turn:
         return True
    elif inputDict[7] == turn and inputDict[5]  == turn and inputDict[3] == turn:
         return True
    elif inputDict[3] == turn and inputDict[6]  == turn and inputDict[9] == turn:
         return True
    else:
         return False
         
def isValid(value):
    isValid = True
    if not value.isnumeric():
        print("숫자가 아닙니다.　다시 입력해주세요.")
        isValid = False
    elif 0 > int(value) and int(value) >= 10 :
        print("0~9 범위의 숫자가 아닙니다.　다시 입력해주세요.")
        isValid = False
    elif checkDuplicate(int(value)) == True:
        print("중복된 위치입니다. 다른 번호를 입력해주세요") 
        isValid = False
    
    return isValid


turn = "X"
count = 1
while True:
    if turn == "X":
        positionX = input("X를 놓을 위치 번호를 선택하세요(1~9)")
        valueX = "X"
        
        if isValid(positionX) == False:
            continue

        setData(int(positionX),valueX)
        printBoard()
        count += 1
        isVictory = confirmVictory(turn)
        if isVictory == True:
            break
        else:
            turn = "O"

    elif turn == "O":
        positionO = input("O를 놓을 위치 번호를 선택하세요(1~9)")
        valueO = "O"

        if isValid(positionO) == False:
            continue

        setData(int(positionO),valueO)
        printBoard()
        count += 1

        isVictory = confirmVictory(turn)

        if isVictory == True:
            break
        else:
            turn = "X"

    if count >= 10:
        break


if count == 10:
    print("무승부입니다")
else:
    print("승리는 '{}'입니다".format(turn))




