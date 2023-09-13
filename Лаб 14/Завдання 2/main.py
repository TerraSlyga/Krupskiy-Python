import numpy as np
import matplotlib.pyplot as plt

years = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
         2017, 2018, 2019, 2020, 2021, 2022]
ukraine_datas = [22824874, 22682516, 22529601, 22365498, 22455476, 22353775, 22246256, 22140771, 22037073, 21940939,
                 21834999, 21670714, 21563197, 21453122, 21345004, 21244133, 21148251, 20585937, 20285701, 20285701]
usa_datas = [148886198, 150113013, 152044690, 154154002, 155503665, 157246174, 157377606, 157357516, 157443452,
             158452840, 158809862, 159540139, 160644681, 162448669, 163971527, 165307010, 167100511, 165641653,
             166189867, 169229171]
np.array(np.int_(years))

np.array(ukraine_datas)

np.array(usa_datas)

plt.plot(years, ukraine_datas, label='Ukraine', color="blue")

plt.plot(years, usa_datas, label='USA', color="yellow")

plt.title('Діаграма робочої сили    ', fontsize=12)  # назва графіка

plt.xlabel('Рік', fontsize=10, color='black')  # позначення вісі абсцис

plt.ylabel('Значення', fontsize=10, color='black')  # позначення вісі ординат

plt.legend()

plt.grid(True)

plt.show()

county = input("Введіть назву країни для побудови діаграми(Україна або США): ")

fig, ax = plt.subplots()

if county.lower() == "україна":
    ax.bar(years, ukraine_datas)
    plt.title("Діаграма робочої сили України", fontsize=15)
if county.lower() == "сша":
    ax.bar(years, usa_datas)
    plt.title("Діаграма робочої сили США", fontsize=15)
plt.xlabel('Рік', fontsize=10, color='black')  # позначення вісі абсцис

plt.ylabel('Значення', fontsize=10, color='black')  # позначення вісі ординат

ax.set_facecolor('seashell')

fig.set_figwidth(19)  # ширина Figure

fig.set_figheight(12)  # висота Figure

plt.show()
