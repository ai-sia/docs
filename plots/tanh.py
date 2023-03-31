import numpy as np
from matplotlib import pyplot as plt

y = np.linspace(-10, 10, 2048)

plt.plot(y, np.tanh(y))

plt.xlabel('y')
plt.ylabel('Aktivierung')
plt.title('Tanh Aktivierungsfunktion')

plt.savefig('img/tanh.png')

plt.show()
