MIN_COORDINATE = 1
MAX_COORDINATE = 8


def main():
    try:
        x1 = int(input("Введите номер столбца первой клетки (1-8): "))
        y1 = int(input("Введите номер строки первой клетки (1-8): "))
        x2 = int(input("Введите номер столбца второй клетки (1-8): "))
        y2 = int(input("Введите номер строки второй клетки (1-8): "))

        if not (MIN_COORDINATE <= x1 <= MAX_COORDINATE and
                MIN_COORDINATE <= y1 <= MAX_COORDINATE and
                MIN_COORDINATE <= x2 <= MAX_COORDINATE and
                MIN_COORDINATE <= y2 <= MAX_COORDINATE):
            print("Ошибка: все координаты должны быть в диапазоне от 1 до 8")
            return

        if x1 == x2 and y1 == y2:
            print("NO")
            return

        delta_x = abs(x1 - x2)
        delta_y = abs(y1 - y2)
        if delta_x == delta_y:
            print("YES")
        else:
            print("NO")

    except ValueError:
        print("Ошибка: введите целые числа от 1 до 8")

def explain_move(x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    print(f"Анализ хода:")
    print(f"Из клетки ({x1}, {y1}) в клетку ({x2}, {y2})")
    print(f"Разность по горизонтали: {delta_x}")
    print(f"Разность по вертикали: {delta_y}")

    if delta_x == delta_y:
        print("Слон может сделать этот ход - клетки на одной диагонали")
    else:
        print("Слон не может сделать этот ход - клетки не на одной диагонали")

main()