import numpy as np
import matplotlib.pyplot as plt
import csv

# Зчитуємо дані з CSV файлу
csv_file = "data.csv"

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Читаємо заголовок

    # Витягуємо дані з рядка
    years, ukraine_datas, usa_datas = zip(*[(int(row[0]), int(row[1]), int(row[2])) for row in reader])

# Конвертуємо списки у numpy arrays
years = np.array(years)
ukraine_datas = np.array(ukraine_datas)
usa_datas = np.array(usa_datas)

# Графік 1
plt.plot(years, ukraine_datas, label='Ukraine', color="blue")
plt.plot(years, usa_datas, label='USA', color="yellow")
plt.title('Діаграма робочої сили', fontsize=12)
plt.xlabel('Рік', fontsize=10, color='black')
plt.ylabel('Значення', fontsize=10, color='black')
plt.legend()
plt.grid(True)
plt.show()

# Графік 2
county = input("Введіть назву країни для побудови діаграми (Україна або США): ")
fig, ax = plt.subplots()

if county.lower() == "україна":
    ax.bar(years, ukraine_datas)
    plt.title("Діаграма робочої сили України", fontsize=15)
elif county.lower() == "сша":
    ax.bar(years, usa_datas)
    plt.title("Діаграма робочої сили США", fontsize=15)

plt.xlabel('Рік', fontsize=10, color='black')
plt.ylabel('Значення', fontsize=10, color='black')
ax.set_facecolor('seashell')
fig.set_figwidth(19)
fig.set_figheight(12)
plt.show()
