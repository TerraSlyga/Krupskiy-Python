import string

if __name__ == '__main__':
    st1: string = input("Введіть речення:\n")
    res = st1.split()
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[j].startswith(res[i][0]) and res[j].endswith(res[i][len(res[i]) - 1]):
                print(f'{res[i]} {res[j]}')