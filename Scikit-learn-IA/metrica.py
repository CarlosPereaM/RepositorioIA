from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#CARGAR EL CONUNTO DE DATOS DE IRIS

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split (iris.data, iris.target, test_size=0.2, random_state=42 ) 

# CREAR EL CLASIFICAR DE VECINOS MAS CERCANOS
clf = KNeighborsClassifier(n_neighbors=3)
#ENTRENAR EL CLASIFICADOR
clf.fit(X_train, y_train)
#PREDECIR LAS ETIQUETAS PARA LOS DATOS DE PRUEBAS
y_pred = clf.predict(X_test)
#CALCULAR LA PRECISION DEL CLASIFICADOR
accuary = accuracy_score(y_test,y_pred)
print('Precisión del clasificador',accuary)
#PREDICCION DEL MODELO
y_pred = clf.predict(X_test)
#CALCULAR MÉTRICAS DE EVALUACIÓN DEL MODELO
accuary  = accuracy_score(y_test,y_pred)
precision= precision_score(y_test,y_pred,average='weighted')
recall   = recall_score(y_test,y_pred,average='weighted')
f1       = f1_score(y_test,y_pred,average='weighted')
print('Precisión del clasificador',accuary)
print('Precision promedio ponderada: ',precision)
print('Recall promedio ponderado', recall)
print('F1-score promedio ponderado: ',f1)

