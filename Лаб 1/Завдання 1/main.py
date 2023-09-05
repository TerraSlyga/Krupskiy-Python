def findNum(a: float, b: float):  # Функція, що повертає число за заданими значеннями а і b
    if a == b:
        return -25
    if a > b:
        return a / b - 1
    if a < b:
        return (pow(a, 3) - 5) / a


if __name__ == '__main__':  # Оголошення головного методу
    a: float = 0  # Ініціалізація змінних
    b: float = 0
    X: float = 0
    while True:  # Цикл для введення чисел (так як в пайтоні немає do{}while, реалізував так)
        a = float(input("Введіть число а:\n"))
        b = float(input("Введіть число b:\n"))
        if a > 0 and b > 0:
            break
        else:
            print("Одне з чисел є від'ємним. Введіть додатні числа\n")
    X = findNum(a, b)  # Виклик функції
    print(X)  # Вивід результату
