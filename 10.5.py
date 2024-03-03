s, f, g = map(int, input().split())
if s >= f and s >= g:
    if f >= g:
        print(s, f, g)
    elif f < g:
        print(s, g, f)
elif f >= s and f >= g:
    if s >= g:
        print(f, s, g)
    elif s < g:
        print(f, g, s)
elif g >= f and g >= s:
    if f >= s:
        print(g, f, s)
    elif f < s:
        print(g, s, f)
