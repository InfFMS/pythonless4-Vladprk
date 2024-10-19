# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
def rimskoe_chislo(num):
    nm = num//1000
    nd = (num-nm*1000)//500
    nc = (num-nm*1000-nd*500)//100
    nl = (num-nm*1000-nd*500-nc*100)//50
    nx = (num-nm*1000-nd*500-nc*100-nl*50)//10
    nv = (num-nm*1000-nd*500-nc*100-nl*50-nx*10)//5
    ni = (num-nm*1000-nd*500-nc*100-nl*50-nx*10-nv*5)
    print("M"*nm, "D"*nd, "C"*nc, "L"*nl, "X"*nx, "V"*nv, "I"*ni, sep='')


rimskoe_chislo(int(input()))
