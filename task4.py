# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
a = int(input())
b = int(input())


def nadi_nod(a, b, m):
    if a % m == 0 and b % m == 0:
        print(m)
    else:
        m -= 1
        nadi_nod(a, b, m)


nadi_nod(a, b, min(a, b))
