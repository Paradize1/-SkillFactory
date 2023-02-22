board = list(range(1, 10)) #Глобальная переменная доски
wins_coords = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)] #Все выйгрышные комбинации

#Делаем игровое поле
def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
    print('-------------')

def take_input(player_token):
    while True:
        value = input('Куда поставить:' + player_token + '?')             #Смотрим, куда игрок хочет поставить
        if not (value in '123456789'):                          #На случай если игрок введёт число не в том диапозоне
            print('Такого числа нет на поле, введите другое!')
            continue
        value = int(value)                                           #Если клетка уже занята
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята!')
            continue
        board[value - 1] = player_token
        break

#Проверка на выйгрыш
def check_win():
    for each in wins_coords:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1 ]
    else:
        return False

def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if count > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'Выйграл!')
                break
        count += 1
        if count > 8:
            draw_board()
            print('Ничья!')
            break

main()


