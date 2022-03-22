# Descargar información utilizando API de Spotify


<a href="https://colab.research.google.com/drive/1luoqdR0EpPSjrg7TMxPcoMRNEq8WRzBl#scrollTo=Sy_WHqYJRiXh" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


**Requisitos previos a ejecutar el notebook:** _se debe tener crear una aplicación en
la página de desarrolladores de Spotify para usar la API_, _ver_ [_acá_](https://developer.spotify.com/).


1. Cargar credenciales:

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID='TU_CLIENTE'
SPOTIPY_CLIENT_SECRET='TU_CLAVE'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
```

2. Descargar features de canciones con las funciones:

```python
# Multiple canciones pasando lista con URI de cada canción
sp.audio_features(['spotify:track:4hdog9vyyqG9pcppG2Izek', 'spotify:track:5mc6EyF1OIEOhAkD0Gg9Lc'])
```

3. Descargar información de artistas:

```python
# Para un artista
sp.artist('spotify:artist:3s398TKZNahAURRacx7oIT')

# Para multiples artistas
sp.artists(['spotify:artist:0X380XXQSNBYuleKzav5UO', 'spotify:artist:3s398TKZNahAURRacx7oIT'])
```

**Adicional:**A

- ¿Cómo obtener los URIs? Se pueden obtener tanto para artistas, listas y
canciones directamente de Spotify, ver [acá](https://community.spotify.com/t5/FAQs/What-s-a-Spotify-URI/ta-p/919201)
- La idea es obtener esta información para una cantidad importante de canciones
y artistas. Estos uri's id los podemos obtener de la base de datos _"The Spotify Million Playlist Dataset Challenge"_.
