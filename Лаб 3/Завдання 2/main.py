import string

def findUniqueLetter(s1:string, s2:string):
    for i in s1:
        if i not in s2:
            print(i, ' ', end='')

if __name__ == '__main__':
    word1: string = input("Введіть слово 1:\n")
    word2: string = input("Введіть слово 2:\n")
    print("Результат: ")
findUniqueLetter(word1, word2)
findUniqueLetter(word2, word1)