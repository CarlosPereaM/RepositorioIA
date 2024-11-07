from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#CARGAR EL CONJUNTO DE DATOS  DE IRIS

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# CREAR EL CLASIFICADOR DE VECINOS MÁS CERCANOS
clf = KNeighborsClassifier(n_neighbors=3)

# ENTRENAR EL CLASIFICADOR
clf.fit(X_train, y_train)

# PREDECIR LAS ETIQUETAS PARA LOS DTOS DE PRUEBA
y_pred = clf.predict(X_test)

# CALCULAR LA PRECISIÓN DEL CLASIFICADOR
accuracy = accuracy_score(y_test, y_pred)
print('Precisión del clasificador:', accuracy)