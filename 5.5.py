height = float(input())
weight = float(input())
bmi = weight / (height / 100)**2
if bmi < 16:
    print('выраженный дефицит массы тела')
elif 16 <= bmi <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= bmi <= 24.99:
    print('норма')
elif 25 <= bmi <= 29.99:
    print('избыточная масса тела')
elif 30 <= bmi <= 34.99:
    print('ожирение первой степени')
elif 35 <= bmi <= 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')
