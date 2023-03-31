import numpy as np
from matplotlib import pyplot as plt


def relu(y):
    return np.maximum(0.0, y)


y = np.linspace(-10, 10, 2048)

plt.plot(y, relu(y))

plt.xlabel('y')
plt.ylabel('Aktivierung')
plt.title('ReLU Aktivierungsfunktion')

plt.savefig('img/relu.png')

plt.show()
