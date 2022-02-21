"""Запускает игру в обратные "крестики-нолики" компьютера с самим собой."""

from tic_tac import *


def display_info() -> None:
    """Выводит в консоль заставку."""
    print('  Здесь играют два компьютера.')
    print('PC_1 - level=1     PC_2 - level=2')
    print('<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>')


def count_the_points(scores: int, lost_player: str) -> int:
    """Возвращает итоговое значение очков и распечатывает результат"""
    scores[lost_player] += 1
    print('<<<<< ОБЩИЙ СЧЕТ ПОРАЖЕНИЙ: >>>>>')
    print(f'       PC_1 - {scores["PC_1"]}  :  PC_2 - {scores["PC_2"]}')
    print('<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>\n')
    return scores


def play(board, players, scores, flags, alpha_list, current_ind, running, dimension, limit) -> bool:
    """
        Внутренний игровой функционал игры от начала до конца. Возвращает булево значение,
        указывающее на возобновление цикла (рестарт игры) или завершение.
    """
    step = 0
    game = True
    while game:
        if players[current_ind] == 'PC_1':
            level = 1
        elif players[current_ind] == 'PC_2':
            level = 2
        step_list = form_step_list(board, flags, current_ind, limit, level)
        cell = choose_random_cell(step_list)

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


def run(dimension: int=10, limit: int=5):
    """Функция выполняет инициализацию параметров игры и запускает процесс выполнения."""
    if dimension < limit:
        limit = dimension
    running = True
    players = ('PC_1', 'PC_2')
    scores = {'PC_1': 0, 'PC_2': 0}
    flags = ['0', 'X']
    alpha_list = list(chr(i) for i in range(65, 65 + dimension))

    while running:
        running = False
        board = [[' ' for _ in range(dimension)] for _ in range(dimension)]

        display_info()
        draw_board(board, alpha_list, dimension)
        print('\n<<<<<<<<<< Start Game >>>>>>>>>>>\n')
        if input('Нажмите Enter, чтобы начать, или "ex", чтобы завершить игру > ') == 'ex':
            sys.exit(0)
        print('Давайте кинем жребий, кто начнет...\n')
        current_ind = choose_first_step(players)
        flags = change_flags(flags, current_ind)
        running = play(board, players, scores, flags, alpha_list, current_ind, running, dimension, limit)


if __name__ == '__main__':
    run(6, 3)
