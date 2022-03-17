# ¿Cómo cargar datos de Kaggle directamente a Google Colab?

<a href="https://colab.research.google.com/drive/1zvyMKfu_SdXnPcF7fXhyeRauK_X4_4qI?usp=sharing" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

**Requisitos previo a ejecutar el notebook:**

1. Se debe tener una cuenta en Kaggle
1. Ir al menu en esquina superior derecha en _account_
1. En la subsección API, dar _click_ en _Create New API Token_
1. Se descargará en sus computadores el archivo `kaggle.json`, el cual contiene sus credenciales

**Instrucciones a realizar una vez que se haya descargado el archivo con las credenciales:**

1. Crear el directorio en el home del disco virtual con el nombre: `.kaggle`, utilizar el siguiente comando: `!mkdir ~/.kaggle` _(*)_
1. Usar la libreria `google.colab` para cargar archivos de nuestro computador al disco remoto, subiremos el archivo `kaggle.json`:
```python
from google.colab import files
files.upload()
```
1. Mover el archivo `kaggle.json` recién subido a la carpeta creada: `!mv kaggle.json ~/.kaggle/`
1. Debemos cambiar los permisos del archivo `kaggle.json` para que la API pueda acceder a las credenciales: `!chmod 600 ~/.kaggle/kaggle.json`
1. Ahora podemos usar los comandos para acceder a kaggle directamente desde Colab, ver el notebook para continuar con el ejemplo 

_(*): Se puede ejecutar comandos de terminal en google colab usando el caracter `!` al inicio_
