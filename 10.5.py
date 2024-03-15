a = int(input())
f_dgt = a % 10
s_dgt = a // 10 % 10
t_dgt = a // 100 % 10
fo_dgt = a // 1000 % 10
if a // 1000 < 10 and f_dgt != s_dgt != t_dgt != fo_dgt:
    if 1900 <= a <= 2050:
        print('ERROR')
    else:
        print('OK')
else:
    print('ERROR')
