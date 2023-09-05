def buildPiramid(num: int): # Функція, для побудування піраміди
    __arr = []
    for i in range(num):
        # Внутрішній цикл для кожного елемента в рядку
        row = []
        for j in range(i):
            row.append(0)  # Додаємо нулі перед основними числами
        for j in range(1, num - i + 1):
            row.append(j)  # Додаємо основні числа
        __arr.append(row)  # Додаємо рядок до піраміди
    return __arr
def drawPiramid(piramid: [[]]): # Функція для малювання піраміди
    for row in piramid:
        print(' '.join(map(str, row))) # Конвертуємо елементи рядка, розділені пробілами, і об'єднуємо їх, для виведення

if __name__ == '__main__':
    n: int = 7
    arr = [[]]
    arr = buildPiramid(n)
    drawPiramid(arr)