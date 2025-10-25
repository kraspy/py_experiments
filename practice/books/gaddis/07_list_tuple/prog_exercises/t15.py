# График еженедельных цен на бензин за 1994 год. Среди исходного кода главы 7 вы
# найдете файл 1994_ Weekly_ Gas_Averages.txt. Он содержит среднюю цену бензина в течение
# каждой недели 1994 года. (В файле 52 строки.) Используя пакет matplotlib,
# напишите программу Python, которая считывает содержимое файла и затем строит либо
# линейный график, либо гистограмму. Не забудьте показать содержательные метки вдоль
# осей х и у, а также метки делений.
from matplotlib import pyplot as plt

with open('1994_Weekly_Gas_Averages.txt') as f:
    gas_prices = [(i, float(price.strip())) for i, price in enumerate(f.readlines())]
    weeks, prices = zip(*gas_prices)

plt.plot(weeks, prices)

plt.grid()
plt.xlabel('Недели')
plt.ylabel('Цены')

plt.show()
