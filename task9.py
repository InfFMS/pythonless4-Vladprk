# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
def interesting_func(num):
    if num == 1:
        print('YES')
    elif num % 2 != 0:
        print('NO')
    else:
        num = num // 2
        interesting_func(num)


interesting_func(int(input()))
