# CC5205-3-proyecto

Proyecto curso CC5205-3, FCFM, Universidad de Chile

Índice con la documentación del proyecto [acá](https://github.com/alcazar90/CC5205-3-proyecto/tree/main/doc)📚.


## Motivación

Los sistemas de recomendación ya son una tecnología ampliamente usada en los 
servicios digitales, desde el _e-commerce_ hasta las plataformas de _streaming_.
El entusiasmo e interes de empresas en perfeccionar esta tecnología se puede
palpar en diversas competencias como la de [Netflix](https://en.wikipedia.org/wiki/Netflix_Prize) y 
[Spotify](hhttps://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).
La idea es acercar la oferta lo máximo posible a los intereses de los usuarios
y/o consumidores. Por un lado, los usuarios ahorran tiempo y frustración evitando
el bombardeo de opciones irrelevantes, y en el mejor de los casos, pueden llegar
a encontrar su próxima pareja, su nueva canción favorita, o la siguiente serie o
película que comentaran en su próxima reunión de amigos. 
Desde el lado comercial el desafio es grande. Los consumidores se encuentran
cada vez más expuestos a una cantidad abismante de información, el ruído en la
atención de los consumidores es extremo, y su tiempo escazo. Los servicios que no
logren orquestar sus catalogos de servicios y productos tendrán desde una mala
impresión hasta la pérdida de sus usuarios; todo esto con impacto
directo en la última línea del estado de resultados. Adicionalmente, hay mayor
competencia en servicios donde este tipo de tecnologias es particularmente
relevante, y que antes gozaban la ventaja de haber sido los primero en mover,
esto es evidente en la industria  de _streaming_, como es el caso para las películas
y series, antes donde estaba solo Netflix ahora podemos ver más de una decena 
de [servicios similares (i.e. hbomax, paramount, disney+)](https://www.wired.com/gallery/best-streaming-services/).
Recomendar a los usuarios contenido significativo para ellos ya no es un _nice to have_,
sino un requisito para seguir siendo relevantes en la industria.

Dentro de este contexto se encuentra la competencia [_"The Spotify Million Playlist
Dataset Challenge"_](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge),
cuyo objetivo fue explorar (adivinen) 1 millón de _playlists_ con el próposito
de investigar relaciones entre _playlists_ y canciones. De esta manera, descubrir
nuevas formas de entender y enriquecer el servicio conocido como _automatic playlist continuation_,
el como bien dice su nombre, permite continuar reproduciendo música una vez que
la lista de canciones haya finalizado, recomendando canciones similares,
basadas en la lista, pero que estén fuera-de-ella.

Los datos que se pueden ver en la sección _Datasets_, presenten una oportunidad 
para "descubrir" nuevos artistas, y más allá del sistema de recomendación en sí,
explorar como categorizar _playlists_ usando otros atributos aparte del genero musical.
Finalmente, tendremos la oportunidad de construir un prótotipo que pueda 
recomendar canciones dado un _playlist_, aprendiendo a menor escala, un caso de
uso relevante en la industria.

El principal beneficio del servicio _automatic playlist continuation_ es evidente,
una experiencia más armonica y completa al escuchar música. Además, los usuarios
podrán descubrir nuevas canciones, con el potencial de ir "reclutandolas" a sus
listas, y agregando a su radar nuevos artistas que puedan ser de su interes.

Especificamente, la tarea del concurso es desarrollar el sistema descrito
en los parrafos anteriores, y se detalla el _input_ esperado y el _output_:

```
Input

A user-created playlist, represented by:
Playlist metadata (see the dataset README)
K seed tracks: a list of K tracks in the playlist, where K can equal 0, 1, 5, 10, 25, or 100.

Output

A list of 500 recommended candidate tracks, ordered by relevance in decreasing order.

```


## Datasets

Los datos utilizados en este proyecto...

Datos descargados a través de la [API de Spotify](https://developer.spotify.com)
donde nos enfocamos en dos tipos de información, que resumiremos en las
siguientes tres tablas:

### Tabla artistas


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
|   |   |   |


### Tabla playlists

Obtener una playlist del usuario: [Get Playlist](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist)


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
