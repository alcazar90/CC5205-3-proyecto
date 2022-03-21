# CC5205-3-proyecto

Proyecto curso CC5205-3, FCFM, Universidad de Chile

Índice con la documentación del proyecto [acá](https://github.com/alcazar90/CC5205-3-proyecto/tree/main/doc)📚.


## Motivación

Los sistemas de recomendación ya es una tecnología ampliamente usada en los 
servicios digitales, desde el _e-commerce_ hasta las plataformas de _streaming_.
El entusiasmo e interes de empresas en perfeccionar esta tecnología se puede
palpar en diversas competencias como la de [Netflix](https://en.wikipedia.org/wiki/Netflix_Prize) y 
[Spotify](hhttps://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).
La idea es acercar la oferta lo máximo posible a los intereses del usuario/consumidor.
Por un lado, los usuarios ahorran tiempo y frustración evitando el bombardeo
de opciones irrelevantes, y en el mejor de los casos, pueden incluso encontrar
su próxima pareja, canción favorita, o la siguiente serie o película que comentaran
en su próxima reunión de amigos. 
Desde el lado comercial el desafio es grande. Los consumidores se encuentran
expuestos cada vez más a una cantidad abismante de información, 
el ruído en la atención de los consumidores es extremo, y su tiempo vital. Los
servicios que no logren orquestar sus catalogos de servicios y productos tendrán
desde una mala impresión hasta la pérdida de sus usuarios; todo esto con impacto
directo en la última línea del estado de resultados. Adicionalmente, hay una
fragmentación en los servicios de _streaming_, como es el caso para las películas
y series, antes donde estaba solo Netflix, ahora podemos ver más de una decena de
[servicios similares](https://www.wired.com/gallery/best-streaming-services/).
No entregar una cartelera relevante, ya no es un extra, sino un "_must_" para 
ser un competidor relevante.

Dentro de este contexto se encuentra la competencia "The Spotify Million Playlist
Dataset Challenge"(https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge),
cuyo objetivo fue explorar (adivinen) 1 millón de _playlists_ con el próposito
de investigar relaciones entre playlists y canciones. De esta manera, descubrir
nuevas formas de entender y enriquecer el servicio conocido como _automatic playlist continuation_,
el como bien dice su nombre, permite continuar reproduciendo música una vez que
la lista haya agotado todas sus canciones, recomendando canciones similares,
basadas en la lista, pero que estén fuera-de-la-lista.

Los datos que se pueden ver en la sección _Datasets_, presenten una oportunidad 
para "descubrir" nuevos artistas, y más allá del sistema de recomendación en sí,
explorar como categorizar playlists usando otros atributos aparte del genero musical.
Finalmente, tendremos la oportunidad de construir un prótotipo que pueda 
recomendar canciones dado un playlist, aprendiendo un caso relevante de uso en
la industria.

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
| acousticness   | float  | Medida de confianza de 0.0 a 1.0 si el canción es acustico. El valor 1.0 representa una alta confianza de que el _track_ sea acustico |
| danceability  | float   | Medida que describe que tan bailable es una canción en base a una combinación de elementos musicales como el tempo, estabilidad de ritmo, entre otros. Un valor de 0.0 es poco bailable y 1.0 muy bailable  |
| duration_ms  | integer  | Duración de la canción en milisegundos  |
| energy  | float  |   |
| instrumentalness  |   |   |
| liveness|   |   |
| loudness  |   |   |
| mode  |   |   |
| speechiness  |   |   |
| tempo  |   |   |
| time_signature  |   |   |
| valence |   |   |
|   |   |   |
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
