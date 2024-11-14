# IMPORTAMOS LA CLASE FASTAPI DE LA LIBRERIA FASTAPI
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
import nltk # Importamos la libreria Optional para volver parametros opcionales

#Crea una instancia de la clase FastAPI 
app = FastAPI()
# ASIGNAMOS EL VALOR DE TITLE A LA INSTANCIA DE LA CLASE FASTAPI
app.title   ="Mi aplicacion con FastAPI" 
app.version = "0.0.1"

movie_list = [
    {
        "id":1,
        "title":"The Shawshank Redemption",
        "year":"1994",
        "rating":9.5
    },
    {
        "id":2,
        "title":"The Godfather",
        "year":"1972",
        "rating":9.2
    },
    {
        "id":3,
        "title":"The Dark Knight",
        "year":"2008",
        "rating":9.0
    },
    {
        "id":4,
        "title":"The Godfather: Part II",
        "year":"1974",
        "rating":9.0
    },
    {
        "id":5,
        "title":"12 Angry Men",
        "year":"1957",
        "rating":8.9
    },
    {
        "id":6,
        "title":"Schindler's List",
        "year":"1993",
        "rating":8.9
    },
    {
        "id":7,
        "title":"The Lord of the Rings: The Return of the King",
        "year":"2003",
        "rating":8.9
    },
    {
        "id":8,
        "title":"Pulp Fiction",
        "year":"1994",
        "rating":8.9
    },
    {
        "id":9,
        "title":"The Good, the Bad and the Ugly",
        "year":"1966",
        "rating":8.8
    },
    {
        "id":10,
        "title":"The Lord of the Rings: The Fellowship of the Ring",
        "year":"2001",
        "rating":8.8
    }

]


@app.get('/',tags=["Home"]) #Definimos una ruta de la clase fastAPI
def message(): # Definimos una función de la ruta
    return HTMLResponse("<h1>_Hello world_</h1>") # Devolvemos un string en la respuesta de la ruta

@app.get('/movies',tags=["Movies"]) #FENIMOS UNA RUTA DE LA CLASE FASTAPI
def get_movies():
    return  movie_list

@app.get('/movies/{id}', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movie(id: int):
    for item in movie_list:
        if item['id'] == id:
            return item
    return[]

# Flitrado de peliculas por categorias
@app.get("/movies/",tags=["Movies"]) 
def get_movies_by_category(category:Optional[str],year:Optional[int]): # Decorador para indicar que es una ruta de la API
    return [movie for movie in movie_list if movie["category"] == category or movie["year"] == year]



#Tokenizar
@app.post("/tokenize") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)


def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})

# para correr la app: uvicorn main:app --reload
# uvicorn nombreApp:app --reload --port 5000 
# swagger: http://127.0.0.1:5000/docs#/