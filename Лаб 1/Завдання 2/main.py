def findClock (b: int):  # Функція, що повертає число ударів
    sum = 0
    for i in range(b + 1):
        sum += i
    return sum

if __name__ == '__main__':  # Оголошення головного методу
    b: int = 15
    print(f'Кількість ударів від 00 до 15 години: {findClock(b)}')

    input('Press ENTER to exit')
