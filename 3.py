# Константы для границ шахматной доски
MIN_COORDINATE = 1
MAX_COORDINATE = 8


def main():

    input_data = input('Введите 4 числа>>> ').split()

    if len(input_data) != 4:
        print("Ошибка: необходимо ввести 4 числа")
        return
    if not all(item.isdigit() for item in input_data):
        print("Ошибка: все данные должны быть целыми числами")
        return

    x1, y1, x2, y2 = map(int, input_data)

    if not (MIN_COORDINATE <= x1 <= MAX_COORDINATE and
            MIN_COORDINATE <= y1 <= MAX_COORDINATE and
            MIN_COORDINATE <= x2 <= MAX_COORDINATE and
            MIN_COORDINATE <= y2 <= MAX_COORDINATE):
        print("Ошибка: все координаты должны быть от 1 до 8")
        return

    sum1 = x1 + y1
    sum2 = x2 + y2

    if (sum1 % 2) == (sum2 % 2):
        print("YES")
    else:
        print("NO")

def explain_cell_color(x1, y1, x2, y2):
    sum1 = x1 + y1
    sum2 = x2 + y2
    color1 = "черный" if sum1 % 2 == 0 else "белый"
    color2 = "черный" if sum2 % 2 == 0 else "белый"

    print(f"\nАнализ цветов клеток:")
    print(f"Клетка ({x1}, {y1}): сумма = {sum1}, цвет = {color1}")
    print(f"Клетка ({x2}, {y2}): сумма = {sum2}, цвет = {color2}")
    print(f"Одинаковый цвет: {color1 == color2}")
main()