"""
array if int
return True if we can partition the array
into ten non-empty parts with equal sums

# Signature

# Tests
[1, 1, 1, 1, 2, 2, 1, 1, 2, 1] -> False
[1, 2, 3] -> False
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] -> True

[1, 1, 1, -1, 2, 1, 1, 1, 1, 1, 1] -> True
[1], ... [-1, 2], [1]

[1, 1, 1, 7, 0, 0, 0, 0, 0, 0] -> False

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] -> True
Для такого случая нужно добавить проверку,
если find_sum == 0, то количество сегментов может быть больше 10,
но


# Solution
Проверить количество элементов, делится ли отрезок на 10.
Найти сумму массива, первого отрезка,
завести счетчик отрезков.
Перекладываю элементы в отрезки, пока не нахожу нужную сумму –> перехожу
к следующему отрезку. Прибавляю на счетчике отрезков 1, пока не дохожу
до 10 отрезков. Тогда возвращаю True, если условия не выполняются,
возвращаю False

Сложность O(n)
"""


def can_ten_parts_equal_sum(arr: list[int]) -> bool:
    arr_sum = sum(arr)

    if len(arr) < 10:
        return False

    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if arr_sum % 10 != 0:
        return False

    find_sum = arr_sum // 10  # 0
    selected_part = 0
    segments = 0

    for num in arr:  # 0
        selected_part += num  # 0 + 0 = 0
        if selected_part == find_sum:  # 0 == 0
            segments += 1  # 0 + 1 = 1
            selected_part = 0
        elif selected_part > find_sum:  # 0 > 0
            return False

    if segments == 10:
        return True
    else:
        return False
