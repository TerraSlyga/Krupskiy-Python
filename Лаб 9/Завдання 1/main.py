def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1path = 'TF8_1.txt'
file2path = 'TF8_2.txt'
file1 = Open(file1path, 'w')  # Створення текстового файлу TF8_1 з символьних рядків різної довжини
if file1:
    file1.write("Це 1 рядок\n")
    file1.write("Другий 2 рядок\n")
    file1.write("Не знаю який рядок(напевно 3)\n")
    file1.write("Кор0ткий рядок\n")
    file1.write("3 рядок\n")
    file1.close()

file1 = Open(file1path, 'r')  # Читання та обробка вмісту файлу TF8_1
file2 = Open(file2path, 'w')

if file1 and file2:

    line_number = 1
    lines = file1.readlines()

    processed_lines = []
    for i, line in enumerate(lines):
        line = line[0:len(line) - 1]
        # Видалення цифр з рядка
        line = ''.join(char for char in line if not char.isdigit())
        # Розбиваємо рядок на підрядки по 10 символів
        sublines = [line[i:i + 10] for i in range(0, len(line), 10)]

        for subline in sublines:
            file2.write(f'{line_number:05d} {subline}\n')
            line_number += 1

    file1.close()
    file2.close()

# в) Читання та друк вмісту файлу TF8_2
file2 = Open('TF8_2.txt', 'r')

if file2:
    for line in file2:
        print(line.strip())
    file2.close()
