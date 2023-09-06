def deleteObj(list2: list):
    list2.pop(2)
    list2.pop(-2)
    return list2

if __name__ == '__main__':
    lenght: int = int(input("Введіть кількість елементів списку:\n"))
    list1 = list()
    for i in range(lenght):
        list1.append(input(f"Введіть елемент {i + 1}:\n"))
    deleteObj(list1)
    print(f"Список після видалення 2 і передостаннього елементу: {list1}")