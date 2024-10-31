# Importamos la biblioteca de pandas y la llamamos 'pd'
import pandas as pd

# Creamos una serie de pandas que es como una lista con etiquetas
# Los valores son nombres de jugadores del PSG
# El indice especifica los números de camisetas de esos jugadores

psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'] #Lista de jugadores
#,index=[1,7,10,30]                                         # Lista de Indices (números de camisetas)
)      

# Creamos un diccionario que asocia números de camisetas con nombres de jugadores
# El diccionario tiene la misma estructura que la serie anterior pero con llaves y valores

psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

# Creamos una Serie de Pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

print(psg_players_dict);

print(psg_players_dict[7])

print(psg_players_dict[0:3])

# Diccionario con datos de jugadores
dict = { 'Jugador' : ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles' : [2, 200, 150, 200]}

# Creamos un DataFrame con el diccionario e índices personalizados
df = pd.DataFrame(dict, index = [1, 7, 10, 30])
# Imprimimos el DataFrame
print(df)