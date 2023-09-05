from cmath import sin
from Cells import findCels

def findNum(a: float):  # Функція, що знаходить число
    return (2 ** 0.5) / 2 * sin(a / 2)


if __name__ == '__main__':  # Оголошення головного методу
    a: float = 0  # Ініціалізація змінних
    n: int = 0

    a = float(input("Введіть число a:\n"))
    n = int(input("Введіть число n:\n"))
    z: float = findNum(a)
    result: int = findCels(n)

    print(f'Результат 1: {z}')
    print(f'Результат 2: {result}')
    input("Закрити програму")
