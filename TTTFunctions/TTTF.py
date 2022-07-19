def display_board(board):
    # Funkcja, ktora przyjmuje jeden parametr zawierajacy biezacy stan tablicy
    # i wyswietla go w oknie konsoli.
    for i in range(len(board)):
        print(board[i])


def enter_move(board):
    # Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
    # prosi uzytkownika o wykonanie ruchu, 
    # sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.
    ok = True
    while ok:
        ruch =  int(input('Wprowadź liczbę\n'))
        n = 0
        if ruch < 1 or ruch > 9:
            print('Błędna liczba!\n')
            continue
        else:
            for i in range(len(board)):
                for j in range(len(board[i])):# print(board[i][j])
                    n = n+1
                    if board[i][j] == ruch:
                        board[i][j] = 'o'
                        ok = False
                    elif n == ruch and (board[i][j] == 'x' or board[i][j] == 'o'):
                        print('Zajete pole!')
                        break

def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.
    wygrana = 'nie'
    if board[0][0] == board[1][1] == board[2][2] == sign:
        wygrana = 'wygrana'
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        wygrana = 'wygrana'
    else:
        for i in range(len(board)):
            j = 0
            if board[i][j] == board[i][j+1] == board[i][j+2] == sign:
                wygrana = 'wygrana'
            elif board[j][i] == board[j+1][i] == board[j+2][i] == sign:
                wygrana = 'wygrana'
    if wygrana == 'nie':
        n = 0
        licznik=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                n = n+1
                if n == board[i][j]:
                    licznik = licznik + 1
        if licznik == 0:
            wygrana = 'remis'
            
    return wygrana

def draw_move(board):
    # Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.
    from random import randrange
    ruch = 0
    ok = True
    while ok:
        ruch = randrange(10)
        while ruch == 0:
            ruch = randrange(10)
        n = 0
        if ruch < 1 or ruch > 9:
            print('Błędna liczba!\n')
            continue
        else:
            for i in range(len(board)):
                for j in range(len(board[i])):# print(board[i][j])
                    n = n+1
                    if board[i][j] == ruch:
                        print(ruch)
                        board[i][j] = 'x'
                        ok = False
                    elif n == ruch and (board[i][j] == 'x' or board[i][j] == 'o'):
                        break
