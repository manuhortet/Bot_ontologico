![Python 3.5.2](https://img.shields.io/badge/python-3.5.2-blue.svg)

# Bot_ontologico

Bot de generación de lenguaje natural simple, dedicado a divagar sobre el sentido de la vida. ![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40Bot_ontologico)




## How to setup

### Dependencias

1. Primero, asegurémonos de tener `pip` instalado y actualizado:

    ```
    pip install --upgrade pip
    ```
    
1. Ahora, únicamente, instalemos [Tweepy](http://www.tweepy.org/), librería de Python con la que accederemos a la API de Twitter:

    ```
    pip install tweepy
    ```
    
    
### Estructura

- Bot_ontologico

  - :file_folder: markovbot 
  - generated_sentences.txt
  - generator.py
  - keys.py (*)
  - poster.py
  - README.md
  - (*)
  
(*) El archivo `keys.py` contiene las claves privadas que conceden a la aplicacion acceso para publicar tweets desde cierta cuenta de Twitter.
  Para obtenerlas debemos crear nuestra aplicación de Twitter desde [este link](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app). Con la aplicación ya creada, desde el Application Manager, debemos buscar el botón _**Create my access token**_ en la pestaña **Permisos**. 
  Las keys que necesitaremos para hacer funcionar este bot están comentadas en el archivo `keys.py`.

(*) Para que el bot sea capaz de generar texto, ha de ser entrenado con archivos .txt, los cuales he obviado. Con cuantos más archivos .txt sea entrenado, mejor será su producción de texto.
[@Bot_ontologico](https://twitter.com/Bot_ontologico) es entrenado únicamente con libros del autor Jean-Paul Sartre (entrenar con la obra de un único autor también mejora la producción, al ser más común la repetición de expresiones y estructuras),
pero podemos entrenar al programa con los archivos .txt que queramos. Solo hemos de añadirlos y editar la variable `books` en el archivo *generator.py*.


### Uso

1. Ejecutando el archivo *generator.py*, el bot generará y escribirá en *generated_sentences.txt* un número de tweets igual a la variable `tweets_to_generate`. 
1. Ejecutando el archivo *poster.py*, el bot publicará los tweets del archivo *generated_sentences.txt*, esperando un número de horas igual al valor de la variable `hours` entre publicación y publicación.

Los tweets son escritos en un archivo y no publicados directamente para darnos la posibilidad de filtrarlos y de decidir el orden de publicación de los mismos.

##

*El código para NLG basado en la cadena de Markov (`markovbot/markovbot.py`) que uso como plantilla es del usuario de GitHub @esdalmaijer*.
**Thank you very much for keeping it public!**

##

*No dudes en pedirme ayuda o explicaciones más detalladas.* *[@manuhortet](https://twitter.com/manuhortet?lang=en)*
