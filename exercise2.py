import os
import sys


def clear_console():  # очистка консоли
    if sys.platform == "linux":
        os.system('clear')
    else:
        os.system('cls')


def check_input(atr_in, arr):  # проверка ввода номера ячейки
    if not atr_in.isdigit():
        print('Вы ввели не число. Повторите ввод.')
        return 0
    else:
        atr_in = int(atr_in)
    if 8 >= (atr_in - 1) >= 0:
        if arr[atr_in - 1].isdigit():
            return atr_in
        else:
            print('Клетка занята, попробуйте еще раз.')
            pause()
            return False
    else:
        print('Нет такой клетки!')
        pause()
        return False


def check_winner(cells_names, steps):  # проверка текущего игрового поля на выигрыш сторон/ничью
    win_cord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 4, 8), (2, 4, 6), (0, 3, 6),
                (1, 4, 7), (2, 5, 8))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(cells_names[c])
        if symbols == ["X", "X", "X"]:
            return "Выиграл игрок 1(Х)!!!!"
        if symbols == ["O", "O", "O"]:
            return "Выиграл игрок 2(0)!!!"
    if steps == 9:
        return "Ничья!!!"
    return False


def win_out(arr, flag):  # вывод выигрышной комбинации игры
    render_field(cells_names)
    print(flag_end)
    pause()


def render_field(arr):  # вывод текущего состояния игрового поля
    clear_console()
    a = '_' * 13 + '\n'
    for i in range(len(arr)):
        a += f'| {arr[i]} '
        if (i + 1) % 3 == 0:
            a += '|\n'
    a += '‾' * 13 + '\n'
    print(a)


def greet():  # вывод приветствие начала игры
    array_greet = '''********************************************************************
*   Здравствуйте! Приветствую вас в игре крестики-нолики!          *
*   В игру играют два игрока, каждый игрок ходит по очереди        *
*   Один игрок управляет крестиком, другой - ноликом               *   
*   Поочередно игроки вводят номер ячейки, куда поставить          *
*   Свой крестик или же нолик. Победит тот игрок, чьи крестики     *   
*   Или нолики займут полностью строку, столбец или диагональ      * 
*                   Приятной игры!!!                               *
********************************************************************\n'''
    print(array_greet)
    pause()


def pause():
    input("Нажмите Enter для продолжения...")


while True:  # цикл начала игры
    clear_console()
    steps = 0
    cells_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    greet()

    while True:  # основной цикл игры

        while True:  # ввод правильных данных игрока Х
            render_field(cells_names)
            p1_input = input("Игрок 1(Х), введите номер ячейки: ")
            in_true = check_input(p1_input, cells_names)
            if in_true:
                steps += 1
                p1_input = in_true
                cells_names[p1_input - 1] = 'X'
                break

        flag_end = check_winner(cells_names, steps)  # проверка на выигрыш после каждого правильного ввода
        if flag_end:
            win_out(cells_names, flag_end)
            break

        while True:  # ввод правильных данных игроком O
            render_field(cells_names)
            p2_input = input("Игрок 2(O), введите номер ячейки: ")
            in_true = check_input(p2_input, cells_names)
            if in_true:
                steps += 1
                p2_input = in_true
                cells_names[p2_input - 1] = 'O'
                break

        flag_end = check_winner(cells_names, steps)
        if flag_end:
            win_out(cells_names, flag_end)
            break
