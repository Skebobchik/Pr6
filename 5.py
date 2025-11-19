
MIN_COORDINATE = 1
MAX_COORDINATE = 8
def main():
    try:
        print("Введите четыре числа от 1 до 8:")
        x1 = int(input("Номер столбца первой клетки: "))
        y1 = int(input("Номер строки первой клетки: "))
        x2 = int(input("Номер столбца второй клетки: "))
        y2 = int(input("Номер строки второй клетки: "))

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

        is_horizontal_move = (y1 == y2)
        is_vertical_move = (x1 == x2)
        is_diagonal_move = (delta_x == delta_y)
        if is_horizontal_move or is_vertical_move or is_diagonal_move:
            print("YES")
        else:
            print("NO")

    except ValueError:
        print("Ошибка: введите целые числа от 1 до 8")

def explain_queen_move(x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    print(f"\nАнализ хода ферзя:")
    print(f"Из клетки ({x1}, {y1}) в клетку ({x2}, {y2})")

    is_horizontal = (y1 == y2)
    is_vertical = (x1 == x2)
    is_diagonal = (delta_x == delta_y)

    print(f"Горизонтальный ход: {is_horizontal}")
    print(f"Вертикальный ход: {is_vertical}")
    print(f"Диагональный ход: {is_diagonal}")

    if is_horizontal or is_vertical or is_diagonal:
        print("Ферзь может сделать этот ход")
    else:
        print("Ферзь не может сделать этот ход")
main()
