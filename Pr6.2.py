karman=int(input("Введите номер кармана:"))
if karman==0:
    print('Карман 0, зеленый')
elif ((1<=karman<=10) or (19<=karman<=28)) and karman % 2 == 0:
    print('карман черни')
elif ((1<=karman<=10) or (19<=karman<=28)) and karman % 2 == 1:
    print('карман красни')
elif ((11<=karman<=18) or (29<=karman<=36)) and karman%2==0:
    print('карман красный')
elif ((11<=karman<=18) or (29<=karman<=36)) and karman % 2 == 1:
    print('карман черни')
else:
    print('ошибка ввода')