a = int(input())
f_dgt = a % 10
s_dgt = a // 10 % 10
t_dgt = a // 100 % 10
fo_dgt = a // 1000 % 10
if 1000 <= a <= 9999:
    if f_dgt == fo_dgt and s_dgt == t_dgt:
        print('Настоящее')
    else:
        print('Кривое')

