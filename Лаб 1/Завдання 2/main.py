def findClock (b: int):  # Функція, що повертає число ударів
    for i in range(b + 1):
        print(f"Ударів в {i} годину: {i}")

if __name__ == '__main__':  # Оголошення головного методу
    b: int = 15
    findClock(b)

    input('Press ENTER to exit')