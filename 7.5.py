n, m, k = map(int, input().split())
if m - k > 1:
    a = m - k - 1
    b = (n - m) + (k - 1)
    if a <= b:
        print(a)
    else:
        print(b)
if k - m > 1:
    a = k - m - 1
    b = (n - k) + (m - 1)
    if a <= b:
        print(a)
    else:
        print(b)
if abs(k - m) == 1:
    print(0)
