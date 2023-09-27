
if __name__ == '__main__':
    n = int(input("Введіть кількість елемнентів:\n"))
    arr = []
    for i in range(n):
        print(f"Введіть елемент {i}:")
        arr.append(int(input()))
    print(f'Мінімальне число: {min(arr)}')
