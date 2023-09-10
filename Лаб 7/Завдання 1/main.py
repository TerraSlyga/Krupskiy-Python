import random
import string

# Лист імен для випадкової генерації
names = ["Анна", "Богдан", "Вікторія", "Дмитро", "Євгенія", "Зоряна", "Ігор", "Катерина", "Лариса", "Максим"]

# Функція для вибору випадкового імені з списку
def get_name(names: list):
    num = random.randint(0, len(names))
    temp = names[num]
    names.pop(num)
    return temp

# Функція для генерації випадкового номера
def generate_random_phone():
    # Генеруємо номер, складаючи його з випадкових цифр
    phone = ''.join(random.choice(string.digits) for _ in range(10))
    return f"+{phone}"

# Функція для заповнення словника іменами з випадковими номерами n раз
def populate_phonebook(phonebook, n):
    for _ in range(n):
        name = get_name(names)
        phone = generate_random_phone()
        add_entry(phonebook, name, phone)

# Функція для виведення на екран всіх значень словника
def display_phonebook(phonebook):
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

# Функція для додавання нового запису до словника
def add_entry(phonebook, name, phone):
    phonebook[name] = phone
    print(f"{name} додано до записника з номером {phone}")

# Функція для видалення запису за ім'ям
def remove_entry(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} видалено з записника")
    else:
        print(f"{name} не знайдено в записнику")

# Функція для пошуку номера за ім'ям
def find_phone_by_name(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Ім'я не знайдено в записнику"

# Функція для пошуку імені за номером телефону
def find_name_by_phone(phonebook, phone):
    for name, number in phonebook.items():
        if number == phone:
            return name
    return "Номер не знайдено в записнику"

if __name__ == "__main__":
    # Створення пустого словника для збереження даних
    phonebook = {}

    # Головний цикл програми
    while True:
        print("\nМеню:")
        print("1. Вивести весь записник")
        print("2. Додати новий запис")
        print("3. Видалити запис за ім'ям")
        print("4. Знайти номер за ім'ям")
        print("5. Знайти ім'я за номером")
        print("6. Заповнити записник випадковими даними")
        print("7. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            print("Весь записник:")
            display_phonebook(phonebook)
        elif choice == "2":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            add_entry(phonebook, name, phone)
        elif choice == "3":
            name = input("Введіть ім'я для видалення: ")
            remove_entry(phonebook, name)
        elif choice == "4":
            search_name = input("Введіть ім'я для пошуку номера: ")
            found_phone = find_phone_by_name(phonebook, search_name)
            if found_phone:
                print(f"Телефон {search_name}: {found_phone}")
            else:
                print(f"{search_name} не знайдено в записнику")
        elif choice == "5":
            search_phone = input("Введіть номер для пошуку імені: ")
            found_name = find_name_by_phone(phonebook, search_phone)
            if found_name:
                print(f"Ім'я для номера {search_phone}: {found_name}")
            else:
                print(f"Номер {search_phone} не знайдено в записнику")
        elif choice == "6":
            n = int(input("Введіть кількість записів для заповнення(max = 10): "))
            populate_phonebook(phonebook, n)
        elif choice == "7":
            print("Дякуємо за використання програми!")
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть опцію з меню.")
