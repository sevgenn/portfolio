"""Приложение крестики-нолики "наоборот".Проигрывает выстроивший в ряд limit одинаковых символов."""

import random
import sys
import time
from typing import List, Tuple, Union
import argparse


def display_info(limit: int) -> None:
    """Выводит информацию об игре с учетом выбранного проигрышного числа q."""
    print('Задача по очереди заполнить поле символами "Х" или "0".\n'
          'Право первого хода определяется случайным образом.\n'
          'Первый игрок использует "Х". Проигрывает тот, кто выстроит в ряд\n'
          f'(по горизонтали, вертикали или диагонали) {limit} одинаковых символов.\n'
          'Размерность поля ограничена от 3х3 до 26х26. Можно выбрать уровень компьютера.\n')


def change_level() -> None:
    """Проверяет корректность ввода данных при выборе уровня."""
    while True:
        try:
            level = int(input('Выберите уровень игры (от 0 до 2) >> '))
            if level not in range(3):
                continue
        except ValueError:
            print('Введите цифры от 0 до 2')
        else:
            break


def draw_board(board: List[List[str]], alpha_list: List[str], dimension: int) -> None:
    """Отрисовывает квадратную матрицу размера nxn с буквенно-цифровым обозначением ячеек."""
    print()
    print(' ' * 5, end='')
    for item in alpha_list:
        print(f' {item}  ', end='')
    print()
    print(' ' * 4 + '-' * 4 * dimension + '-')
    for i in range(dimension):
        print(f'{i + 1:>3} |', end='')
        for j in range(dimension):
            print(f' {board[i][j]} |', end='')
        print()
        print(' ' * 4 + '-' * 4 * dimension + '-')


def let_me_see(timeout=0.02):
    """Декорирует вывод компьютера."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Один момент...')
            for _ in range(40):
                print('>', end='')
                time.sleep(timeout)
            print()
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@let_me_see()
def choose_first_step(players: Tuple[str]) -> int:
    """Рандомно выбирает, кто ходит первый и возвращает его индекс в списке."""
    ind = random.choice((0, 1))
    print(f'{players[ind]} ходит первым. Его знак - "X"\n')
    return ind


def change_flags(flags: List[str], current_ind: int) -> List[str]:
    """Возвращает список игровых символов в таком виде, чтобы первый игрок всегда ходил с "Х"."""
    if flags[current_ind] != 'X':
        flags = flags[::-1]
    return flags


def transform_input(alpha_list: List[str], address_str: str) -> Union[Tuple[int], bool]:
    """Возвращае адрес ячейки, преобразованный в матричные индексы i, j, или False, если адрес вне диапазона."""
    addr = address_str.replace(' ', '').upper()
    if addr[0] in alpha_list and int(addr[1:]) in range(1, 27):
        h_ind = int(addr[1:]) - 1
        v_ind = alpha_list.index(addr[0])
        return h_ind, v_ind
    return False


def is_cell_occupied(board: List[List[str]], cell: Tuple[int]) -> bool:
    """Возвращает булево значение в зависимости от того, пробел в ячейке или другой символ."""
    return not board[cell[0]][cell[1]].isspace()


def input_user_cell(board: List[List[str]], alpha_list: List[str]) -> Tuple[int]:
    """Возвращает корректный адрес ячейки, введенной пользователем."""
    while True:
        user_input = input('Введите позицию в формате "e 2"\nили "ex", чтобы выйти > ')
        if user_input == "ex".lower() or user_input == "уч".lower():
            print('Игрок покинул игру.')
            sys.exit()
        cell = transform_input(alpha_list, user_input)
        if not cell:
            print('Некорректный индекс. Будьте внимательны.')
            continue
        if is_cell_occupied(board, cell):
            print('Ячейка уже занята.')
            continue
        break
    return cell


def print_comment_to_step(player: str, alpha_list: List[str], cell: Tuple[int]) -> None:
    """Выводит информацию, кто и какой ход сделал."""
    alpha = alpha_list[cell[1]]
    num = cell[0] + 1
    print(f'{player} пошел на {alpha}{num}')


def make_step(board: List[List[str]], cell: Tuple[int], flag: str) -> List[List[str]]:
    """Помещает символ игрока в выбранную ячейку и возвращает измененную матрицу.
        :rtype: list"""
    board[cell[0]][cell[1]] = flag
    return board


def get_main_diagonal_of_matrix(board: List[List[str]], cell: Tuple[int]):
    """Возвращает диагональ, проходящую через заданную ячейку параллельно главной диагонали."""
    len_row = len(board)
    i_top_left = cell[0] - cell[1]
    i_top_left = i_top_left if i_top_left >= 0 else 0
    j_top_left = cell[1] - cell[0]
    j_top_left = j_top_left if j_top_left >= 0 else 0
    i_down_right = (len_row - 1) - j_top_left
    length = i_down_right - i_top_left + 1
    return (board[i_top_left + k][j_top_left + k] for k in range(length))


def get_side_diagonal_of_matrix(board: List[List[str]], cell: Tuple[int]):
    """Возвращает диагональ, проходящую через заданную ячейку параллельно побочной диагонали."""
    len_row = len(board)
    i_top_right = cell[0] + cell[1] - (len_row - 1)
    i_top_right = i_top_right if i_top_right >= 0 else 0
    j_top_right = cell[0] + cell[1]
    j_top_right = j_top_right if j_top_right <= (len_row - 1) else (len_row - 1)
    i_down_left = j_top_right
    length = i_down_left - i_top_right + 1
    return (board[i_top_right + k][j_top_right - k] for k in range(length))


def is_lost(board: List[List[str]], cell: Tuple[int], flag: str, limit: int) -> bool:
    """"
        Проверяет повторение limit раз подряд заданного символа в ряду, столбце и диагоналях
        матрицы, проходящих через заданную ячейку, и возвращает результат в виде булева значения.
    """
    result = False

    if flag * limit in ''.join(board[cell[0]]):
        result = True
    board_t = list(zip(*board))
    if flag * limit in ''.join(board_t[cell[1]]):
        result = True
    if flag * limit in ''.join(get_main_diagonal_of_matrix(board, cell)):
        result = True
    if flag * limit in ''.join(get_side_diagonal_of_matrix(board, cell)):
        result = True
    return result


def test_losing(board: List[List[str]], cell: Tuple[int], flag: str, limit: int) -> bool:
    """Присваивает значение ячейке и проверяет будет ли в этом положении проигрыш."""
    board[cell[0]][cell[1]] = flag
    return is_lost(board, cell, flag, limit)


def form_step_list(board: List[List[str]], flags: str, pc_ind: int, limit: int, level: int) -> List[Tuple[int]]:
    """
        Возвращает список непроигрышных ячеек, которые не перекрывают слабые позиции противника.
        При отсутствии таковых возвращает список непроигрышных ячеек.
        Если и таких нет, возвращает список свободных ячеек. Уровень формируемого списка
        определяется значением уровня level.
        """
    empty_list = []
    possible_list = []
    the_best_list = []
    board_test = [row[:] for row in board]
    opponent_ind = (pc_ind + 1) % 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                cell = (i, j)
                empty_list.append(cell)
                if (level in [1, 2]) and not test_losing(board_test, cell, flags[pc_ind], limit):
                    possible_list.append(cell)
                    if level == 2 and not test_losing(board_test, cell, flags[opponent_ind], limit):
                        the_best_list.append(cell)
                board_test[i][j] = ' '
    if the_best_list:
        return the_best_list
    if possible_list:
        return possible_list
    return empty_list


@let_me_see()
def choose_random_cell(step_list: List[Tuple[int]]) -> Tuple[int]:
    """Возвращает рандомно выбранную свободную ячейку."""
    return random.choice(step_list)


def is_game_over() -> bool:
    """Возвращает отказ или согласие игрока на рестарт игры."""
    restart = input('Сыграем еще раз? (y/n) >> ')
    return restart == 'y'


def count_the_points(scores: int, lost_player: str) -> int:
    """Возвращает итоговое значение очков и распечатывает результат"""
    scores[lost_player] += 1
    print('<<<<< ОБЩИЙ СЧЕТ ПОРАЖЕНИЙ: >>>>>')
    print(f'       PC - {scores["PC"]}  :  human - {scores["HUMAN"]}')
    print('<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>\n')
    return scores


def play(board, players, scores, flags, alpha_list, current_ind, running, dimension, limit, level) -> bool:
    """Внутренний игровой функционал игры от начала до конца. Возвращает булево значение,
        указывающее на возобновление цикла (рестарт игры) или завершение."""
    step = 0
    game = True
    while game:
        if players[current_ind] == 'PC':
            step_list = form_step_list(board, flags, current_ind, limit, level)
            cell = choose_random_cell(step_list)
        else:
            cell = input_user_cell(board, alpha_list)

        print_comment_to_step(players[current_ind], alpha_list, cell)
        make_step(board, cell, flags[current_ind])
        draw_board(board, alpha_list, dimension)
        print('\n' * 5)

        if is_lost(board, cell, flags[current_ind], limit):
            print(f'"{flags[current_ind]}" проиграли.')
            print('Game over\n')
            scores = count_the_points(scores, players[current_ind])
            game = False

        step += 1
        if game and step == dimension * dimension:
            print('Ничья')
            game = False

        current_ind = (current_ind + 1) % 2
        if not game:
            running = is_game_over()
            print('\n' * 5)
    return running


def run(dimension: int=10, limit: int=5) -> None:
    """Функция выполняет инициализацию параметров игры и запускает процесс выполнения."""
    if dimension > 26:
        dimension = 26
    if dimension < 3:
        dimension = 3
    if dimension < limit:
        limit = dimension
    running = True
    players = ('PC', 'HUMAN')
    scores = {'PC': 0, 'HUMAN': 0}
    flags = ['0', 'X']
    alpha_list = list(chr(i) for i in range(65, 65 + dimension))

    while running:
        level = 0
        running = False
        board = [[' ' for _ in range(dimension)] for _ in range(dimension)]

        display_info(limit)
        draw_board(board, alpha_list, dimension)
        change_level()
        print('\n<<<<<<<<<< Start Game >>>>>>>>>>>\n')
        if input('Нажмите Enter, чтобы начать, или "ex", чтобы завершить игру > ') == 'ex':
            sys.exit(0)
        print('Давайте кинем жребий, кто начнет...\n')
        current_ind = choose_first_step(players)
        flags = change_flags(flags, current_ind)
        running = play(board, players, scores, flags, alpha_list, current_ind, running, dimension, limit, level)


if __name__ == '__main__':
    run()
