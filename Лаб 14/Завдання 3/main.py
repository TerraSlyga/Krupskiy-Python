import numpy as np
import matplotlib.pyplot as plt
import csv

# Зчитуємо дані з CSV файлу
csv_file = "data.csv"

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Читаємо заголовок

    # Витягуємо дані з рядка
    years, usa_datas = zip(*[(int(row[0]), float(row[1])) for row in reader])

# Конвертуємо списки у numpy arrays
years = np.array(years)
usa_datas = np.array(usa_datas)

# Графік
fig, ax = plt.subplots()
ax.pie(usa_datas, labels=years, autopct='%1.1f%%')
ax.axis("equal")

plt.title("GDP per capita (current US$)")
plt.show()
