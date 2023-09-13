import numpy as np
import matplotlib.pyplot as plt

print("Діаграма побудована")
x = np.linspace(0, 1, 50)
f1 = 15 * np.sin(10 * x) * np.cos(3 * x)

plt.plot(x, f1, label='Y(x)=15*sin(10*x)*cos(3*x)', color="red", linewidth=2)
plt.xlabel("Х")
plt.ylabel("Y")
plt.title("Діаграма графіка функції Y(x)=15*sin(10*x)*cos(3*x), x=[-3...3]", fontsize = 12)
plt.legend()
plt.grid(True)
plt.show()
