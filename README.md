## CC5205-3: Yet Another Spotify Song Recommender 🎵

Proyecto curso CC5205-3, FCFM, Universidad de Chile

Índice con la documentación del proyecto [acá](https://github.com/alcazar90/CC5205-3-proyecto/tree/main/doc)📚.

**Tabla de contenidos**

- [Motivación](#motivación)
- [Dataset](#dataset)
- [Análisis Exploratorio](#análisis-exploratorio)
	- [Preguntas & Problemas](#preguntas-y-problemas)

## Motivación

Hoy en día, el boom tecnológico ha hecho que el mercado global sea cada vez más competitivo al 
momento de captar clientes. Dentro de esta competitividad, han surgido nuevas estrategías y 
algoritmos para poder lograr que la experiencia del consumidor sea la más grata y sencilla. 
¿Cómo logra un nuevo servicio posicionarse en el mercado? ¿Cómo logra mantener a sus usuarios satisfechos?. Hoy existen varias metodologías para esto, particularmente hablaremos de los sistemas de recomendación.

Los sistemas de recomendación son una tecnología ampliamente usada en los servicios digitales, desde el _e-commerce_ hasta las plataformas de _streaming_. Qué mejor que, al comprar tus zapatillas favoritas, o al ver una buena pelicula, exista un algoritmo que te vaya recomendando productos o experiencias similares a las que acabas de comprar o ver. 

Como explicamos anteriormente, el entusiasmo e interés de empresas en perfeccionar esta tecnología se puede palpar en diversas competencias y servicios que utilizamos diariamente, como el de [Netflix](https://en.wikipedia.org/wiki/Netflix_Prize) y [Spotify](hhttps://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).

La idea principal es acercar la oferta lo máximo posible a los intereses de los usuarios y/o consumidores. Por un lado, los usuarios ahorran tiempo y frustración evitando el bombardeo de opciones irrelevantes, y en el mejor de los casos, pueden llegar a encontrar su próxima pareja, su nueva canción favorita, o la siguiente serie o película que comentaran en su próxima reunión de amigos.

Desde el lado comercial, el desafio es grande. Los consumidores se encuentran cada vez más expuestos 
a una cantidad abismante de información, el ruído en la atención de los consumidores es extremo, 
y su tiempo escazo. Las empresas que no logren orquestar sus catálogos de servicios o productos 
tendrán, en el mejor de los casos, un reclamo, y en el peor, la fuga de sus usuarios y clientes; Todo esto con impacto directo en 
la última línea del estado de resultados. Además, hay cada vez mayor competencia en servicios donde 
este tipo de tecnologias es particularmente relevante, y que antes algunas compañías gozaban de la ventaja de haber sido _first movers_. Esto es evidente en la industria  de _streaming_, como es el caso para las 
películas y series. Al principio, solo teníamos Netflix, en cambio ahora podemos ver más de una decena de
[servicios similares (i.e. Hbomax, Hulu, Paramount, Disney+)](https://www.wired.com/gallery/best-streaming-services/).
Recomendar a los usuarios contenido significativo para ellos ya no es un _nice to have_, sino un 
requisito para seguir siendo relevantes en la industria.

Dentro de este contexto, se encuentra la competencia [_"The Spotify Million Playlist Dataset 
Challenge"_](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge), cuyo 
objetivo fue explorar (adivinen) 1 millón de _playlists_ con el próposito de investigar relaciones 
entre _playlists_ y canciones. De esta manera, descubrir nuevas formas de entender y enriquecer el 
servicio conocido como _automatic playlist continuation_, el cual como bien dice su nombre, permite 
continuar reproduciendo música una vez que la lista de canciones haya finalizado, recomendando canciones 
similares basadas en la lista, pero que estén fuera-de-ella.

Los datos que se pueden ver en la sección _Datasets_, presenten una oportunidad para "descubrir" nuevos
artistas, y más allá del sistema de recomendación en sí, explorar cómo categorizar _playlists_ usando 
otros atributos aparte del género musical. Finalmente, tendremos la oportunidad de construir un prototipo que pueda 
recomendar canciones dado un _playlist_, aprendiendo a menor escala, un caso de uso relevante en la industria.

El principal beneficio del servicio _automatic playlist continuation_ es el que busca toda empresa hoy en día,
mejorar la experiencia del consumidor a través de una experiencia más armonica y completa al escuchar música. 
Además, los usuarios podrán descubrir nuevas canciones, con el potencial de ir "reclutándolas" a sus listas, 
y agregando a su radar nuevos artistas que puedan ser de su interes.

Específicamente, la tarea del curso es desarrollar el sistema descrito en los parrafos anteriores, y se detalla 
el _input_ esperado y el _output_:

```
Input

A user-created playlist, represented by:
Playlist metadata (see the dataset README)
K seed tracks: a list of K tracks in the playlist, where K can equal 0, 1, 5, 10, 25, or 100.

Output

A list of 500 recommended candidate tracks, ordered by relevance in decreasing order.

```

## Dataset

El _dataset_ utilizado en este proyecto es de carácter público y proviene de dos fuentes:

1. El _dataset_ del millón de _playlists_ de Spotify cuya curatoría de datos
se encuentra disponible para descargar en las plataformas competitivas de [Aircrowd](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge) y [Kaggle](https://www.kaggle.com/datasets/adityak80/spotify-millions-playlist). Esta información fue liberada por Spotify para fines del concurso y no es posible recopilarla directamente a través de su API.
1. Información sobre artistas y canciones que descargamos desde la [API de Spotify](https://developer.spotify.com) para desarrolladores con el propósito de complementar y enriquecer los datos del punto anterior.


Adicionalmente, en el directorio [`/data`](https://github.com/alcazar90/CC5205-3-proyecto/tree/main/data) de este repositorio se encuentran
versiones de las tablas de información para 20.000 _playlists_, con la información necesaria para complementar los artistas y canciones de estas. El 
objetivo de esta muestra es realizar pruebas y experimentaciones de manera
rápida previo a escalar los análisis al _dataset_ completo.

* [Muestra al azar de 100.000 listas](https://drive.google.com/file/d/1pWUP8YJ4BryPhzprn24_VP-EZOv_4jLN/view?usp=sharing)
* [Tracks Feature](https://drive.google.com/file/d/1RDbXdqha6usjy_i2exrVFfQE1cXgGsSv/view?usp=sharing)

En las siguientes subsecciones se encuentra el _codebook_ para las 3 tablas de información que conforman el dataset.


### Tabla playlists

Obtener una playlist del usuario: [Get Playlist](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist)

Tabla desagregada por canciones de la playlist

| Feature  | Tipo de variable | Descripción  |
|----------|------------------|---------------|
| name | object | Nombre de la playlist |
| colabborative | boolean | Si es una lista colaborativa o no |
| pid | int | Identificador de la lista |
| modified_at | datetime | Fecha de modificación de la lista |
| num_tracks | int | Cantidad de canciones en la lista |
| num_albums | int | Cantidad de álbumes en la lista |
| num_followers | int | Cantidad de álbumes en la lista |
| num_edits | int | Cantidad de ediciones a la lista |
| duration_ms | int | Duración de cada canción en milisegundos |
| num_artists | int | Cantidad de artistas en la lista |
| description | string | Descripción de la lista |
| pos | int | Posición de la canción en la lista |
| artist_name | string | Nombre del artista de la canción |
| track_uri | string | URL para obtener información de la canción |
| artist_uri | string | URL para obtener información del artista la canción |
| track_name | string | Nombre del track |
| album_uri | string | URL para obtener información del álbum de la canción |
| album_uri | string | Nombre del álbum de la canción |

### Tabla artistas
| Feature  | Tipo de variable | Descripción  |
|----------|------------------|---------------|
| external_urls | object | URL externas conocidas para este artista. |
| external_ursl.spotify | string | Variable que contiene la URL que redirecciona al perfil del artista. |
| followers | object | Contiene información acerca del artista. |
| followers.href | string | Esto siempre se establecerá en nulo, ya que la API web no lo admite en este momento. |
| followers.total | int | Número total de seguidores. |
| genres | list of strings | Lista de los géneros a los que está asociado el artista. Si aún no se ha clasificado, la lista estará vacía. |
| href | string | Link que proporciona los detalles del artista (que son estos mismos datos).
| id | string | El Spotify ID del artista. |
| images | list of objects | El objeto contiene imágenes del artista en varios tamaños. |
| images.url | string | La URL de la imagen. |
| images.height | int | La altura de la imagen en píxeles. |
| images.width | int | El ancho de la imagen en píxeles. |
| name | string | El nombre del artista. |
| popularity | int | Es la popularidad del artista representada como número. El valor estará entre 0 y 100, siendo 100 el más popular. La popularidad del artista se calcula a partir de la popularidad de todas las pistas del artista. |
| type | string | El tipo de objeto (por defecto será 'artist'). |
| uri | string | El [URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) de Spotify. |

### Tabla canciones

Es posible extraer para cada canción los _audio features_ que se encuentran
documentados [acá](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features).

| Feature  | Tipo de variable | Descripcción  |
|----------|------------------|---------------|
| acousticness   | float  | Medida de confianza de 0.0 a 1.0 si la canción es acustica. El valor 1.0 representa una alta confianza de que la canción sea acustica. |
| danceability  | float   | Medida que describe que tan bailable es una canción en base a una combinación de elementos musicales como el tempo, estabilidad de ritmo, entre otros. Un valor de 0.0 significa poco bailable y 1.0 muy bailable.  |
| duration_ms  | integer  | Duración de la canción registrada en milisegundos.  |
| energy  | float  | La energía es una medida de 0.0 a 1.0 y representa una medida de percepcción de intensidad y actividad. Generalmente, las canciones energeticas se siente rápidas, fuertes y ruidosas. Ejemplo, el _death metal_ tiene alta energía, mientras que un preludio de Bach tiene un medición baja en la escala.   |
| instrumentalness  | float  | Predice si una canción no contiene vocales. "Ooh" and "Aah" son tratados como instrumentales en este contexto. El Rap o canciones con palabras habladas son claramente "vocales". Mientras más cercano es el valor de `instrumentalness` a 1.0, mayor es la probabilidad de que la canción no contenga vocales.|
| liveness| float  | Detecta la presencia de audiencia/público en la grabación. Valores altos de `liveness` representan una mayor probabilidad de que la canción haya sido tocada en vivo. |
| loudness  | float  | El volumen total de la canción registrado en decibeles (dB). El volumen es promediado a lo largo de toda la canción y es útil para comparar el volumen relativo entre canciones. Los valores en general se encuentran entre -60 y 0 db.|
| mode  | integer  | Indica la modalidad (mayor o menor) de una canción. Mayor es representado por 1 y menor por 0.  |
| speechiness  | float  | Detecta la presencia de vocales en una canción. Si la grabación tiene gran contenido de vocales (e.g. audiolibro, poesía, conversación), más cercano el atributo a 1.0. Valores sobre 0.66 describen canciones que probablemente esten hechas completas de palabras habladas. Valores entre 0.33 y 0.66 describen canciones que contienen música y letra, separadas o juntas, incluye casos como la música rap. Valores bajo 0.33 mayormente música y canciones sin vocales. |
| tempo  | float   | `tempo` estimado total de una canción en _beats_ por mínutos (BPM). En términos musicales, el `tempo` es la velocidad, o fase de una pieza, y se deriva directamente del _beat_ promedio de duración. |
| time_signature  | float  | Un estimado del compás. Es una convención que especifica cuantos _beats_ hay en cada línea (o medida). El compás tiene un rango desde el 3 al 7, indicando el compás de "3/4" al "7/4".|
| valence | float  | Una medida que va del 0.0 al 1.0 y describe la "positiividad" musical de una canción. Canciones con alto `valence` suenan más positivas (e.g. feliz, alegre, euforico), mientras que canciones con poco `valence` suenan más negativas (e.g. triste, depresivo, furioso).  |
| key  | integer  | Indica la nota fundamental de la escala musical en la que está la canción. A cada semitono se le asigna un valor distinto. Explícitamente, para canciones en Do (C), key=0, Do sostenido (C#), key=1, Re (D), key=2, y así sucesivamente. Por esto tiene 12 valores posibles  |


## Análisis Exploratorio

**TODO:** Las figuras see encuentran almacenadas en subdirectorio [`fig/`](https://github.com/alcazar90/CC5205-3-proyecto/tree/main/fig).

Para agregar imagenes en esta parte, solo se debe agregar:

> #![](fig/nombre_foto.png)

El siguiente es un template de como podríamos ir agregando los insights.


**Objetivo del análisis:** Forma de visualizar las canciones por playlist según atributo músical.

![](fig/heatmap_loudness.png)

Preguntas y problemas: podríamos agregar directamente los posibles problemas y preguntas. La desventaja de esto sería que es atómico y no mezcla los distintos tipos de análisis.

**OLI: Propongo que el EDA lo escribamos con la siguiente estructura. Yo (Diego) hice más de la parte de features así que me voy a enfocar en esa, pero puedo ayudar también en las otras secciones. Según tengo entendido, Gianina analizó Playlists y Cristóbal analizó Playlists y Features, y Felipe con Christopher analizaron Artists. Podríamos repartirnos así las secciones para no chocar tanto. Igual me ofrezco para ayudar donde se necesite.**

El análisis exploratorio de los datos lo realizamos por separado para las distintas tablas del dataset para poder entender mejor como están distribuidas las distintas variables, ya que cada tabla posee distintas estructuras.

### Tabla Playlists

**TODO**

### Tabla Artistas

**TODO**

### Tabla Features

#### Análisis univariado

Esta última tabla contiene valores numéricos que describen características de las canciones que posiblemente nos serán útiles para clasificar o predecir preferencias por las canciones. Posiblemente estarán correlacionadas con los géneros musicales o con las playlists (Canciones con features similares se encuentren en las mismas playlists)

Podemos notar que cuatro de las variables (energy, tempo, danceability y valence) tienen una distribución simétrica y equitativamente repartida en el rango (similar a una distribución normal). Probablemente estas variables nos serán útiles para clasificar las canciones y no se les debería realizar ninguna transformación.

> #![](fig/features_c_nice.png)

Dos de las variables (duration y loudness) parecen tener distribuciones equitativas pero presentan outliers que ensucian los datos. En particular, duration tiene outliers al existir canciones con duraciones muy superiores al promedio. En estas variables sería necesario eliminar outliers.

> #![](fig/features_c_outliers.png)

Otras variables tienen distribuciones muy cargadas hacia ciertos valores, particularmente valores bajos. En acousticness una minoría de las canciones posee entre 0.2 y 1.0 mientras la mayoría posee valores muy cercanos a cero. Algo similar sucede con speechiness y liveness y el caso es extremo en instrumentalness. Pareciese ser que estas características son pseudo binarias, donde si posee la característica tendrá valores entre ~0.2 y 1 con probabilidades similares. Podría ser necesario realizar alguna transformación matemática de estos datos o simplemente convertirlos a variables categóricas binarias.

> #![](fig/features_c_uneven.png)

Finalmente, las variables mode, time_signature y key toman una cantidad limitada de valores. Mode al tomar sólo 2 valores debería probablemente ser considerado como variable categórica. Podemos notar que la mayoría de las canciones está en tonalidad mayor. Key está uniformemente repartida por lo que podría ser útil en la clasificación, y al tomar múltiples valores no sería necesario considerarla variable categórica. Time signature es un caso especial. Notamos que hay outliers correspondientes posiblemente a datos erroneos (No existen compás 0/4 o 1/4). También sería necesario transformarla, ya que no hace sentido considerarla una cantidad.

> #![](fig/features_c_categoric.png)

#### Análisis multivariado



### Preguntas y Problemas


## Integrantes

```
@misc{CC5205-3-proyecto,
  authors = {Alcázar, Cristóbal}, {Callpa, Felipe}, {Cortez, Diego}, {Salomó, Gianina}, {Stears, Christopher}
  title = {Por definiir...},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/alcazar90/CC5205-3-proyecto}},
}
```
