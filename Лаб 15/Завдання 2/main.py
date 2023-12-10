import pandas as pd

data = pd.read_csv("comptagevelo2010.csv")

# Конвертуємо стовпець "Date" у формат дати з рядка у форматі "%d/%m/%Y" та додаємо стовпець місяця
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data["Month"] = data["Date"].dt.month

# Обчислюємо загальну популярність велодоріжок у кожному місяці, знаходимо найпопулярніший місяць загалом
sum_total = data.groupby("Month")[["Rachel / Papineau", "Berri1","Maisonneuve_1", "Maisonneuve_2", "Brébeuf", "Parc",
                                   "CSC (Côte Sainte-Catherine)", "PierDup"]].sum().sum(axis=1)
most_popular_month_in_total = sum_total.idxmax()

print(f"\nНайпопулярніший місяць у велосипедистів: {most_popular_month_in_total} з кількістю : {sum_total.max()}")
