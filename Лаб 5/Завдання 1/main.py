def findMin(arr:list):
    minimum: int = 999999999
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum

if __name__ == '__main__':
    n: int = int(input("Введіть кількість елемнентів:\n"))
    arr = []
    for i in range(n):
        print(f"Введіть елемент {i}:")
        arr.append(int(input()))
    print(f'Мінімальне число: {findMin(arr)}')
