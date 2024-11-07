# CARGA DE PAQUETES Y FUNCINOES PARA GENERAR GRÁFICOS
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

rango = np.random.RandomState(0)
x     = np.linspace (0, 10, 500)
y     = np.cumsum(rango.randn(500, 6), 0)

# GRAFICAR LOS DATOS
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

