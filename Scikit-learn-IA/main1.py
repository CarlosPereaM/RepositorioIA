from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#CARGAR EL CONJUNTO DE DATOS CALIFORNIA HOUSTING
California = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split (California.data, California.target, test_size=0.2, random_state=42 ) 

#CREAR EL MODELO DE REGRESION LINEAL
model  = LinearRegression()

#ENTRENAR EL MODELO
model.fit(X_train, y_train)

#PREDECIR LOS PRECIOS DE LAS VIVIENDAS PARA LOS DATOS DE PRUEBAS
y_pred = model.predict(X_test) 

#CALCULAR EL ERROR CUADRATICO MEDIO
mse = mean_squared_error(y_test, y_pred)
print('Error cuadrático medio', mse)