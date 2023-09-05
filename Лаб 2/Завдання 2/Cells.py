def findCels(n: int): # Функція, що знаходить кількість амеб
    res: int = 1
    for i in range(n//3):
        res *= 2
    return res