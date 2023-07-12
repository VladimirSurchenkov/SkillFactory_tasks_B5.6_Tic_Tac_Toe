# Создания поля
field = [[' '] * 3 for i in range(3)]
field[0][1] = 'X'
field[0][2] = 'X'
field[0][0] = 'x'


# Игравое поле
def show():
    print()
    print("    0 | 1 | 2 |")
    print('---------------')
    for i, row in enumerate (field):
        row_str = f"{i} | {' | '.join(row)}"
        print(row_str)
        print('---------------')
    print()
show()

# Координаты
# def ask():
#     while True:
#         x,y = map(int, input('Ваш ход: ').split())
#         if 0 <= x <= 2 and 0 <= y <=2 :
#             if field[x][y] == ' ':
#                 return x, y
#             else:
#                 print('Клетка занята!')
#         else:
#             print('Координаты вне диапазона!')
# ask()

#
# def ask():
#     while True:
#         x,y = map(int, input('Ваш ход: ').split())
#         if 0 > x or x > 2 or 0 > y or y > 2:
#             print('Координаты вне диапазона!')
#             continue
#
#         if field[x][y] != ' ':
#             print('Клетка занята!')
#             continue
#     return x, y

def ask():
    while True:
        cords = input('Ваш ход: ').split()

        if len(cords) !=2:
            print('Введите 2 координаты! ')
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа: ')
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != " ":
            print('Клетка занята!')
            continue
        return x, y
ask()

