import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
    
"""
    Считываем данные с файла, добавляем имена для столбцов
"""
df = pd.read_csv('task8.tsv', sep='\t', header=None)

X, Y = df[0], df[1]

x = list(X)
y = list(Y)

"""
    Приравнивание значений nan = 0
"""
for i in range(len(y)):
    if math.isnan(y[i]):
        y[i] = 0
    else:
        y[i] = y[i]
"""
    Отображение координат точек из данных файла
"""
plt.scatter(x, y, c ='black', label = u'Данные из файла')

#print(df)

#Создаем массив из списков 
#array - функция, создающая объект типа ndarray;
#для использования в np.polyfit - работа + возврат массива
numpy_x = np.array(x)
numpy_y = np.array(y)

x1 = list(range(743))

"""
    Отображении функций в зависимости от степени полиномы от 1 до 5
    poly1d - функция помогает определить полиномиальную функцию (составление многочлена взависимости от степени полиномы)
"""

func1 = np.poly1d(np.polyfit(numpy_x, numpy_y, 3))
plt.plot(x1, func1(x1), label = u'Изображение полинома 3-ей степени')
func2 = np.poly1d(np.polyfit(numpy_x, numpy_y, 4))
plt.plot(x1, func2(x1), label = u'Изображение полинома 4-ой степени')
func3 = np.poly1d(np.polyfit(numpy_x, numpy_y, 10))
plt.plot(x1, func3(x1), label = u'Изображение полинома 10-ой степени')

plt.title('Полиномиальные графики')
plt.grid(True)
plt.legend()
plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.show()
