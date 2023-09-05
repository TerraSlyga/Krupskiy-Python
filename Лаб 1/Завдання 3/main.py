def printPiramid(a: int):  # Функція, що друкує пірамідку
    for i in range(a, -1, -1):
        for j in range(a, i, -1):
            print(j, ' ', end='')
        print()


if __name__ == '__main__':  # Оголошення головного методу
    a: int = 0  # Ініціалізація змінних
    a = abs(int(input("Введіть число стовпчиків:\n")))  # abs щоб виключити можливість введення від'ємного числа
    printPiramid(a)
