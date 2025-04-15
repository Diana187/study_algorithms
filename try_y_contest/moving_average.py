"""
Скользящее среднее

Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает q от i запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.


# Signature
list[int], list[int] -> list[int]

# Tests
5
1 2 3 4 5  -> 3
5

1 + 2 + 3 + 4 + 5 = 15/5 = 3


# Solution




"""

seconds = int(input())
requests = list(map(int, input().split()))
sliding_window = int(input())


def moving_avarage():
    pass


# print(" ".join([str(x) for x in seq]))
