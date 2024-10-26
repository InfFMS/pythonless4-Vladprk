# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
def func_razlozeni(num, i):
    def prostoe(n):
        delit = 0
        for j in range(1, int((n**0.5)+2)):
            if n % j == 0:
                delit += 1
        if delit == 1:
            return True
        else:
            return False

    while num % i == 0:
        print(i)
        num //= i
    if not prostoe(num):
        i += 1
        func_razlozeni(num, i)
    else:
        if num != 1:
            print(num)


func_razlozeni(int(input()), 2)
