"""
array of int
return True if we can partition the array
into three non-empty parts with equal sums.

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104

# Signature
list[int] -> bool

# Tests
[1, 2, 3] -> False

[1, 1, 1, 2, 1, 3] -> True
[1], [1], [1, 2, 1, 3]
[1, 1], [1, 2], [1, 3]
[1, 1, 1], [2, 1], [3]

[-1, 2, 1, 3] -> False

# Sulution
Взять сумму всего списка, разделить её на 3 – это сумма, которую мы ищем.
Нахожу первую часть, которая равна сумме, которую ищем.
Также нахожу вторую часть, перекладывая элементы поочередно из третьей части.
Пока в третьей части не останется 1 элемент (непустой остаток).
Сравниваю сумму третьей части с искомой.

Только я не совсем понимаю, какая тут сложность
O(n)?


(Взять сумму всего списка, разделить её на 3 – это сумма, которую мы ищем.
Нахожу первую часть, которая равна сумме искомой сумме.
Потом ищу отрезок, сумма которого = искомой сумме х2,
проходясь по остальным элементам)
Тут будет такая же сложность


"""


# это какой-то кошмар со сложностью
def can_three_parts_equal_sum(arr: list[int]) -> bool:
    arr_sum = sum(arr)
    if arr_sum % 3 != 0:
        return False

    find_sum = arr_sum // 3
    first_part = 0

    for i in range(len(arr) - 2):
        first_part += arr[i]
        if first_part == find_sum:
            for i_2 in range(i + 1, len(arr) - 1):
                second_part = 0
                second_part += arr[i_2]
                if second_part == find_sum:
                    third_part = 0
                    for i_3 in range(i_2 + 1, len(arr) - 1):
                        third_part += arr[i_3]
                        if third_part == find_sum:
                            return True
    return False
