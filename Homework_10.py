import matplotlib.pyplot as plt
import numpy as np

# Упражнение 1
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()

# Упражнение 2
x = np.arange(0, 2 ,0.1)
y = x**2

plt.plot(x, y, label="y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функций")
plt.legend()
plt.show()

# Упражнение 3
x = [1,3,5,7,9]
y = [5,2,7,8,2]
width = 1

plt.bar(x,y,width, label = "Пример гистограммы")
plt.legend()
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("Гистограмма")
plt.show()

