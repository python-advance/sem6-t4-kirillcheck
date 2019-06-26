#Задание №1.
#Используя свободные источники (bn.ru, avito.ru и т.д.), собрать данные о ценах на недвижимость, 
#выставленную на продажу в разных районах города. Преобразовать данные в формат csv. 
#Разработать скрипт для визуализации данных, используя библиотеку matplotlib. 
#Для визуализации использовать тип “точечная диаграмма” (scatterplot).

%matplotlib inline

import pandas as pd 
import matplotlib.pyplot 
import numpy as np

"""
    Загрузка исходных данных, добавление имен столбцов 0 и 1
"""
df = pd.read_csv('data.csv', header = None) 
x, y = df[0], df[1] 
#print(df)

"""
    Строем линейную функцию по двум точка, также
    можно использовать линейную функцию y = 2x -10
"""
x1,y1 = [0,22.5],[0,25]


"""
    Визуализация данных
"""

#fig = plt.plot(x, y, 'r*', label = u'Данные из файла') Отображение с помощью plot

fig = plt.scatter(x, y, s = x, c ='red', label = u'Данные из файла') 
fig1 = plt.plot(x1, y1, 'b', label = u'Линейная функция y = 2x -10') 

plt.savefig('plot.png', format='png', dpi=100)
plt.title('Построение графика')
plt.legend()
plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.grid(True)
