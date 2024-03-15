a = int(input())
f_dgt = a % 10
s_dgt = a // 10 % 10
t_dgt = a // 100 % 10
fo_dgt = a // 1000 % 10
if a // 1000 < 10:
    if f_dgt != s_dgt and f_dgt != t_dgt and f_dgt != fo_dgt and s_dgt != t_dgt and s_dgt != fo_dgt and t_dgt != fo_dgt:
        if 1900 <= a <= 2050:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')
