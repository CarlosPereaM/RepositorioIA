#IMPORTAMOS LA LIBRERIA PANDAS, FUNDAMENTAL PARA ANALISIS DE DATOS
import pandas as pd

#DEFINIMOS LA RUTA DEL ARCHIVO CSV QUE CONTIENEN LOS DATOS
#SI EL ARCHIVO ESTA EN EL MISMO DIRECTORIO BASTA CON PONER EL NOMBRE DEL ARCHIVO
path        = 'Sesion_2/DRAGONBALL-LEGENDS.csv' 
dragon_data = pd.read_csv(path,encoding='utf8')
print(type(dragon_data))
print("------")
print(dragon_data.head())