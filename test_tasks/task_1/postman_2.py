"""Решение методом Литтла."""

from typing import Tuple, Union, List
import numpy as np
import timeit


def calculate_distance(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> float:
    """Принимает координаты двух точек на плоскости и возвращает расстояние между ними."""
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def get_min_row(matrix: List[List[float]], points: list) -> Union[int, float]:
    """
    Принимает двумерную матрицу и координаты ячейки. Возвращает минимальное значение
    из всех соседних ячеек в ряду.
    """
    return min(x for ind, x in enumerate(matrix[points[0]]) if ind != points[1])


def get_min_column(matrix: List[List[float]], points: list) -> Union[int, float]:
    """
    Принимает двумерную матрицу и координаты ячейки. Возвращает минимальное значение
    из всех соседних ячеек в столбце.
    """
    return min(x for ind, x in enumerate(matrix[:, points[1]]) if ind != points[0])


def subtract_min_from_rows(matrix: List[List[float]]) -> None:
    """
    Вычисляет минимальное значение в каждой строке двумерной матрицы
    и вычитает это значение из строки.
    """
    for i in range(len(matrix)):
        minimum = min(matrix[i])
        matrix[i] -= minimum


def subtract_min_from_columns(matrix: List[List[float]]) -> None:
    """
    Вычисляет минимальное значение в каждом столбце двумерной матрицы
    и вычитает это значение из столбца.
    """
    for i in range(len(matrix)):
        minimum = min(matrix[:, i])
        matrix[:, i] -= minimum


def find_max_weight_element(matrix: List[List[float]], zero_list: list) -> Tuple[Union[int, int]]:
    """
    Принимает матрицу и список нулевых элементов (координаты).
    Возвращает координаты ячейки с максимальным весом.
    """
    max_zero = 0
    max_x = 0
    max_y = 0
    for item in zero_list:
        min_sum = get_min_row(matrix, item) + get_min_column(matrix, item)
        if min_sum > max_zero:
            max_zero = min_sum
            max_x = item[0]
            max_y = item[1]
    return max_x, max_y


def find_min_distance(matrix: List[List[float]], row: list, col: list, result: list=[]) -> list:
    """
    Принимает двумерную матрицу и списки точек обхода. Рекурсивно возвращает список элементов,
    соответствующих минимальным дугам обхода.
    """
    if len(matrix) < 2:
        result.append((row[0], col[0]))
        return result
    # Вычитаем из строк минимальные значения:
    subtract_min_from_rows(matrix)
    # Вычитаем из столбцов минимальные значения:
    subtract_min_from_columns(matrix)
    # Получаем индексы нулевых элементов:
    ind_zero = np.argwhere(matrix == 0)
    # Находим нулевую клетку с максимальной оценкой:
    max_x, max_y = find_max_weight_element(matrix, ind_zero)
    # Добавляем путь:
    result.append((row[max_x], col[max_y]))
    # Расставляем запреты:
    matrix[max_y][max_x] = np.inf
    # Удаляем строку и столбец:
    matrix = np.delete(matrix, max_x, axis=0)
    matrix = np.delete(matrix, max_y, axis=1)
    # Удаляем использованные точки:
    del row[max_x]
    del col[max_y]
    return find_min_distance(matrix, row, col)


def sort_list_by_tuples(raw_list: list) -> list:
    """
    Возвращает список кортежей отсортированный по возрастанию так, что первый элемент последующего
    равен последнем элементу предыдущего.
    """
    if len(raw_list) == 1:
        return raw_list
    raw_list.sort()
    sorted_lst = [raw_list[0]]
    raw_list.remove(raw_list[0])
    k = 0
    while len(raw_list) > 0:
        for item in raw_list:
            if item[0] == sorted_lst[k][1]:
                sorted_lst.append(item)
                raw_list.remove(item)
                k += 1
    return sorted_lst


def fill_distance_list(matrix: List[List[float]], route_list: list) -> list:
    """Возвращает список элментов (расстояний) матрицы, соответствующих переданному списку обхода."""
    dist_lst = []
    for item in route_list:
        dist = matrix[item[0]][item[1]]
        dist_lst.append(dist)
    return dist_lst


def format_result_string(lst_1: list, lst_2: list) -> str:
    """Принимает список и возвращает стоку в формате для данной задачи."""
    result_str = ''
    for i in range(len(lst_1)-1):
        result_str += f'{lst_1[i]}[{lst_2[i]}] --> '
    result_str += f'{lst_1[-1]}[{lst_2[-1]}] = {sum(lst_2)}'
    return result_str


def create_matrix(points: dict, quantity: int) -> List[List[float]]:
    """Принимает словарь точек с координатами и возвращает двумерную матрицу размерностью nxn."""
    matrix_zero = np.zeros((quantity, quantity))
    matrix_zero[np.diag_indices_from(matrix_zero)] = np.inf
    for i in range(quantity - 1):
        for j in range(i+1, quantity):
            matrix_zero[i][j] = calculate_distance(points[i], points[j])
    matrix = matrix_zero + matrix_zero.transpose()
    return matrix


def main(data: dict) -> None:
    """Основная функция запуска."""
    # Словарь координат точек:
    points = {x: y for x, y in enumerate(list(data.keys()))}
    # Формирование рабочей матрицы:
    quantity = len(points)
    matrix = create_matrix(points, quantity)
    # Неизменяемая копия матрицы:
    start_matrix = matrix.copy()
    # Списки точек маршрута:
    row = list(range(quantity))
    col = list(range(quantity))
    # Список минимальных дуг обхода:
    result = find_min_distance(matrix, row, col)
    result_lst = sort_list_by_tuples(result)
    # Список соответсвующмх расстояний:
    dist_lst = fill_distance_list(start_matrix, result_lst)
    result_str = format_result_string(result_lst, dist_lst)
    print(result_str)


if __name__ == '__main__':

    DATA = {
        (0, 2): 'Почтовое отделение',
        (2, 5): 'Ул. Грибоедова',
        (5, 2): 'Ул. Бейкер стрит',
        (6, 6): 'Ул. Большая Садовая',
        (8, 3): 'Вечнозелёная Аллея',
    }

    # start_time = timeit.default_timer()
    main(DATA)
    # print(timeit.default_timer() - start_time)
