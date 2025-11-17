temperature = float(input("Введите температуру тела (указано в цельсиях):"))
pressure= int(input("укажите верхнее давление:"))
pulse=int(input("укажите свой пульс:"))

if 37>=temperature>=36 and 130>=pressure>=110 and 100>=pulse>=60:
    print('Йоу, у вас все хорошо!')
elif 35<=temperature<=38 and 105<=pressure<=140 and 55<=pulse<=110:
    print("легкое недомогание")
else:
    print("Необходим врач")