a = int(input())
if a <= 100:
    if a % 10 == 1 and a != 11:
        print(f'{a} попугай')
    elif 5 <= a <= 20 or 25 <= a <= 30 or 35 <= a <= 40 or 45 <= a <= 50:
        print(f'{a} попугаев')
    elif 55 <= a <= 60 or 65 <= a <= 70 or 75 <= a <= 80 or 85 <= a <= 90:
        print(f'{a} попугаев')
    elif 95 <= a <= 100:
        print(f'{a} попугаев')
    else:
        print(f'{a} попугая')