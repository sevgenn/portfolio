"""Решение задачи "коммивояжера" полным переборома."""

from typing import Tuple
from itertools import permutations
import timeit
import cProfile


def calculate_distance(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> float:
    """Принимает координаты двух точек на плоскости и возвращает расстояние между ними."""
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def create_distance_dict(points: dict) -> dict:
    """Принимает словарь с координатами точек и возвращает словарь расстояний между ними."""
    dist_dict = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            dist_dict[(i, j)] = dist_dict[(j, i)] = calculate_distance(points[i], points[j])
    return dist_dict


def format_result_string(formatted_list: list) -> str:
    """Принимает список и возвращает стоку в формате для данной задачи."""
    result_str = ''
    for i in range(len(formatted_list) - 2):
        if i < (len(formatted_list[0]) - 1):
            result_str += f'({formatted_list[0][i]}, {formatted_list[0][i + 1]})' \
                          f'[{formatted_list[i + 1]}] --> '
        else:
            result_str += f'({formatted_list[0][-1]}, {formatted_list[0][0]})' \
                          f'[{formatted_list[i + 1]}] = {formatted_list[-1]}'
    return result_str


def find_min_combination(dist_dict: dict, quantity: int) -> list:
    """
    Принимает словарь расстояний между точками (включая маршрут туда и обратно:
    {(0,2): 123, (2,0): 123}) и количество всех точек.
    Возвращает список из кортежа с комбинацией самого короткого маршрута, соответствующих расстояний
    между точками и суммой маршрута.
    """
    base = range(quantity)
    matrix = []
    min_dist = 1e6
    for item in filter(lambda x: x[0] == 0, permutations(base)):
        row = [item]
        last_ind = int(item[-1])
        for i in range(len(item) - 1):
            dist = dist_dict[(item[i], item[i + 1])]
            row.append(dist)
        dist = dist_dict[(0, last_ind)]
        row.append(dist)
        sum_dist = sum(row[1:])
        if sum_dist < min_dist:
            row.append(sum_dist)
            min_dist = sum_dist
            matrix = row[:]
    return matrix


def main(data: dict) -> None:
    """Основная функция запуска программы."""
    # Словарь координат точек:
    points = {x: y for x, y in enumerate(list(data.keys()))}

    # Словарь расстояний между всеми точками, чтобы в дальнейшем не считать расстояние каждый раз заново
    dist_dict = create_distance_dict(points)

    matrix = find_min_combination(dist_dict, quantity=len(points))

    result = format_result_string(matrix)
    print(result)


if __name__ == '__main__':
    ###################### Исходные данные: ##########################
    DATA = {
        (0, 2): 'Почтовое отделение',
        (2, 5): 'Ул. Грибоедова',
        (5, 2): 'Ул. Бейкер стрит',
        (6, 6): 'Ул. Большая Садовая',
        (8, 3): 'Вечнозелёная Аллея',
    }

    main(DATA)
    # print(timeit.timeit("main(DATA)", setup="from __main__ import main, DATA", number=1))
    # cProfile.run('main(DATA)')
