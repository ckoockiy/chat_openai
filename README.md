CHAT_OPENAI

Script para realizar conexion con la api de openai y el texto que devuelve openai lo convierto a voz utilizando gtts

Instalación

1.Clonar el repositorio

2.Instalar los paquetes requeridos: pip install -r requirements.txt

3.Configurar la variable de entorno OPENAI_API_KEY con tu clave de API de OpenAI


Uso

Ejecutar el script main.py con el comando python main.py

Introducir el texto para generar una respuesta de OpenAI

Esperar a que el programa genere la respuesta en voz

Configuración de la API de OpenAI

Para utilizar la API de OpenAI, necesitas crear una cuenta y obtener una clave de API.

A continuación, debes configurar la variable de entorno OPENAI_API_KEY con tu clave de API.

Puedes hacerlo en tu archivo .bashrc o .zshrc, o en el archivo activate de un entorno virtual.

export OPENAI_API_KEY="tu_clave_de_API"

Créditos
OpenAI por su plataforma de inteligencia artificial

gTTS por su librería de texto a voz
