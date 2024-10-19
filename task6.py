# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
m, n = map(int, input().split())


def sokrashenie(m, n):
    def nadi_nod(a, b, m):
        if m == 1:
            return 'exit'
        if a % m == 0 and b % m == 0:
            return m
        else:
            m -= 1
            nadi_nod(a, b, m)
    delit = nadi_nod(m, n, min(m, n))
    if delit == 'exit':
        if n != 1:
            print(f'{m}/{n}')
        else:
            print(m)
    else:
        m = m // delit
        n = n // delit
        sokrashenie(m, n)


sokrashenie(m, n)