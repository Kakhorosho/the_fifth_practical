f_year = int(input())
s_year = int(input())
t_year = int(input())
count = 0
if f_year == s_year:
    count += 1
if s_year == t_year:
    count += 1
if t_year == f_year:
    count += 1
print(count)
