import random

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |"," ",board[0][1]," ","|  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |"," ",board[1][1]," ","|  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |"," ",board[2][1]," ","|  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        numer=int(input("Wykonaj swój ruch:"))
        for i in range(3):
            for j in range(3):
                if board[i][j]==numer:
                    board[i][j]='O'
                    return board

def make_list_of_free_fields(board):
    wolne_pola=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O' or board[i][j]=='X':
                continue
            else:
                wolne_pola.append((i,j))
    return wolne_pola

def victory_for(board, sign):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==sign:
            return sign
    for j in range(3):
        if board[0][j]==board[1][j]==board[2][j]==sign:
            return sign
    if board[0][0]==board[1][1]==board[2][2]==sign:
        return sign
    if board[0][2]==board[1][1]==board[2][0]==sign:
        return sign
    return 0

def draw_move(board):
    wolne_pola=make_list_of_free_fields(board)
    lista_wolnych_numerow=[]
    for i in range(len(wolne_pola)):
        lista_wolnych_numerow.append(board[wolne_pola[i][0]][wolne_pola[i][1]])
    los=random.choice(lista_wolnych_numerow)
    for i in range(3):
        for j in range(3):
            if board[i][j]==los:
                board[i][j]='X'
    return board

board=[[1,2,3],[4,'X',6],[7,8,9]] #UTWORZENIE PLANSZY
suma=9 #SPRAWDZANIE REMISU
while True:
    display_board(board)
    if victory_for(board,'X')=='X':
        print("Wygrałeś")
        break
    if victory_for(board,'O')=='O':
        print("Przegrałeś")
        break
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X' or board[i][j]=='O':
                suma=suma-1
    if suma==0:
        print("Remis!")
        break
    suma=9
    board=enter_move(board)
    display_board(board)
    board=draw_move(board)
    


