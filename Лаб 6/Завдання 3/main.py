
if __name__ == '__main__':
    text = input("Введіть текст: ").lower()  # Приймаємо введений текст і перетворюємо його на малий регістр

    # Створюємо множини для літер, які зустрічаються більше одного разу і ті, що зустрічаються по одному разу
    repeating_letters = set()
    unique_letters = set()

    # Проходимося по кожній літері у тексті і додаємо їх до відповідних множин
    for letter in text:
        if letter.isalpha():  # Перевіряємо, чи є символ літерою
            count = text.count(letter)  # Рахуємо кількість входжень літери в текст
            if count >= 2:
                repeating_letters.add(letter)
            elif count == 1:
                unique_letters.add(letter)

    # Виводимо результати
    print("Літери, які входять в текст не менше двох разів:", ', '.join(repeating_letters))
    print("Літери, які входять в текст по одному разу:", ', '.join(unique_letters))
