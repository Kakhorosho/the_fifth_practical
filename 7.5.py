f_year = int(input())
s_year = int(input())
t_year = int(input())
if f_year == s_year or s_year == t_year or t_year == f_year:
    if s_year == t_year:
        if t_year == f_year:
            print(2)
        else:
            print(1)
    else:
        if t_year == f_year:
            print(1)
        else:
            if f_year == s_year:
                print(1)
            else:
                print(0)
else:
    print(0)
