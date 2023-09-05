from cmath import sin


def findNum(a: float):  # Функція, що знаходить число
    return (2 ** 0.5) / 2 * sin(a / 2)

def findCels(n: int): # Функція, що знаходить кількість амеб
    res: int = 1
    for i in range(n//3):
        res *= 2
    return res


if __name__ == '__main__':  # Оголошення головного методу
    a: float = 0  # Ініціалізація змінних
    n: int = 0


    a = float(input("Введіть число a:\n"))
    n = int(input("Введіть число n:\n"))
    z: float  = findNum(a)
    result: int = findCels(n)

    print(f'Результат 1: {z}')
    print(f'Результат 2: {result}')
    input("Закрити програму")
