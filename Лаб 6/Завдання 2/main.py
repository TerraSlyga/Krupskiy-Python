def findMax5(list2: list):
    __resultList = list()
    for _ in range(5):
        __resultList.append(max(list2))
        list2.remove(max(list2))
    return __resultList


if __name__ == '__main__':
    lenght: int = int(input("Введіть кількість елементів списку:\n"))
    list1 = list()
    for i in range(lenght):
        list1.append(input(f"Введіть елемент {i + 1}:\n"))

    print(f"Список 5 максимальних значень{findMax5(list1)}")
