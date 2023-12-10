import pandas as pd

# Ваш словник
contact_book = {
    "Запис1": {"Ім'я": "Іван", "Номер телефону": 380987654321},
    "Запис2": {"Ім'я": "Слава", "Номер телефону": 380955550088},
    "Запис3": {"Ім'я": "Петро", "Номер телефону": 380661112233},
    "Запис4": {"Ім'я": "Колян", "Номер телефону": 380501234567},
    "Запис5": {"Ім'я": "Саша", "Номер телефону": 380731919191},
    "Запис6": {"Ім'я": "Вася", "Номер телефону": 380447788990},
    "Запис7": {"Ім'я": "ПродамГараж", "Номер телефону": 380682345678},
    "Запис8": {"Ім'я": "Саша", "Номер телефону": 380444444444},
    "Запис9": {"Ім'я": "ВалераШашлик", "Номер телефону": 380990011223},
    "Запис10": {"Ім'я": "Сімен", "Номер телефону": 380777888999}
}

# Перетворення словника в датафрейм
df = pd.DataFrame(contact_book).T

# Виведення датафрейму на екран
print("Датафрейм:")
print(df)

# Агрегація і групування даних
grouped_data = df.groupby('Ім\'я').agg({'Номер телефону': ['count', 'min', 'max']})

# Виведення результату групування на екран
print("\nГрупування та агрегація:")
print(grouped_data)
