n = int(input('Количество кнатов: '))
sikl = n / 29
gal = sikl / 17
sikl_new = abs(int(gal) - gal)*17
knat_new = abs(int(sikl_new) - sikl_new)*29
print(f'Количество сиклей: {sikl:.3f}')
print(f'Количество галлеонов: {gal:.3f}')
print(f'Стоимость в размере {int(gal)} галлеонов, {int(sikl_new)} сиклей и {int(knat_new)} кнатов')