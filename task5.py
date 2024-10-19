# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
def unuseful_and_forgotten_sad_function_because_slices_are_exist(a):
    mad_str = a % 10
    if a//10 == 0:
        return str(mad_str)
    else:
        return str(mad_str) + unuseful_and_forgotten_sad_function_because_slices_are_exist(int((a - mad_str)/10))


print(unuseful_and_forgotten_sad_function_because_slices_are_exist(int(input())))
