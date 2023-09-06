import json

# Функція для завантаження даних з JSON файлу
def Load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("\nФайл не знайдено")


# Функція для збереження даних в JSON файл
def Save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Функція для виведення вмісту JSON файлу
def Print_json_data(file_name):
    datas = Load_data(file_name)
    if datas:
        for data in datas:
            print(data)
    else:
        print("\nJSON файл порожній")


# Функція для додавання нового запису у JSON файл
def Add_entry(file_name, name, number):
    data: list = Load_data(file_name)
    entry = {"Прізвище": name, "Номер телефону": number}
    data.append(entry)
    Save_data(file_name, data)


# Функція для видалення запису за номером телефону
def Delete_entry_by_phone(file_name, number):
    data = Load_data(file_name)
    data = [entry for entry in data if entry["Номер телефону"] != number]
    Save_data(file_name, data)


# Функція для пошуку даних за номером телефону
def Find_entry_by_phone(file_name, number):
    data = Load_data(file_name)
    for entry in data:
        if entry["Номер телефону"] == number:
            return entry["Прізвище"]
    print("\nНеправильно введений номер, або запису не існує")
    return None


# Функція для пошуку номера телефону за прізвищем
def Find_phone_by_surname(file_name, name):
    data = Load_data(file_name)
    for entry in data:
        if entry["Прізвище"] == name:
            return entry["Номер телефону"]
    print("\nНеправильно введене ім'я, або запису не існує")
    return None


if __name__ == "__main__":
    phonebook_file = "phonebook.json"

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис за номером телефону")
        print("4. Пошук інформації за номером телефону")
        print("5. Пошук номера телефону за прізвищем")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            Print_json_data(phonebook_file)

        elif choice == "2":
            surname = input("Введіть прізвище: ")
            phone_number = input("Введіть номер телефону: ")
            Add_entry(phonebook_file, surname, phone_number)
            print("Запис додано до JSON файлу.")

        elif choice == "3":
            phone_number = input("Введіть номер телефону для видалення: ")
            Delete_entry_by_phone(phonebook_file, phone_number)
            print("Запис видалено з JSON файлу.")

        elif choice == "4":
            phone_number = input("Введіть номер телефону для пошуку інформації: ")
            surname = Find_entry_by_phone(phonebook_file, phone_number)
            if surname:
                print(f"Прізвище: {surname}")

        elif choice == "5":
            surname = input("Введіть прізвище для пошуку номера телефону: ")
            phone_number = Find_phone_by_surname(phonebook_file, surname)
            if phone_number:
                print(f"Номер телефону: {phone_number}")

        elif choice == "6":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")
