import numpy as np


def greet():
    print("Введите")
    print("ряд и")
    print("пробел,")
    print("столбец")
    print("и Inter")


# начальные данные
def create_board():
    return np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])


# Вывод в консоль на шаге
def show(board):
    print("  1 2 3")
    for i, row in enumerate(board):
        _str = row
        print(i + 1, *_str)


# Проверка выигрышных вариатров
def check(board):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграли крестики !")
            return True
        if symbols == ["o", "o", "o"]:
            print("Выиграли нолики !")
            return True
    return False


# Изменить дописать в борд
def board_option_input(board, player):
    while True:
        cords = input(" Ввод: ").split()
        if len(cords) != 2:
            print(" Введите 2 числа ")
            continue
        x1, y1 = cords
        if not (x1.isdigit()) or not (y1.isdigit()):
            print(" Это не числа! ")
            continue
        plus_cords = [int(i) - 1 for i in cords]
        x, y = plus_cords

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Числа вне диапазона 1-2-3! ")
            continue
        if board[x][y] != "-":
            print(" Клетка занята! ")
            continue
        board[x][y] = player
        break

    return board


# start
def play_game():
    board, winner, step_game = create_board(), 0, 0
    greet()
    show(board)
    while not winner:
        for player in ['x', 'o']:
            step_game += 1
            board_option_input(board, player)
            show(board)
            print("Сделан " + str(step_game) + " ход")
            winner = check(board)
            if winner:
                break


play_game()
