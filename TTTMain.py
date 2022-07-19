import time
from TTTFunctions.TTTF import display_board, enter_move, victory_for, draw_move

#Tworzenie i wyświetlenie tablicy
board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)

#1 krok - zaczyna komputer - zawsze od pola 5
print("Komputer zaczyna:\n")
print("5")
board[1][1] = 'x'
display_board(board)

#dopóki zmienna gra nie przyjmie warosci x gra sie toczy
gra = ''
while gra != 'x':
    enter_move(board)
    display_board(board)
    wynik = victory_for(board, 'o')
    if wynik == 'wygrana':
        print('Gratulacje wygrałeś! Koniec gry!')
        break
    elif wynik == 'remis':
        print('Remis! Koniec gry!')
        break
    print("Teraz ruch komputera!\n")
    time.sleep(1)
    draw_move(board)
    time.sleep(1)
    display_board(board)
    wynik = victory_for(board, 'x')
    if wynik == 'wygrana':
        print('Przegrałeś! Koniec gry!')
        break
    elif wynik == 'remis':
        print('Remis! Koniec gry!')
        break
    gra = input("Czy chcesz kontunować? Jeśli nie, wciśnij x, jeśli tak naciśnij dowolny przycisk\n")
     
