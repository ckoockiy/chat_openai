from gtts import gTTS
from playsound import playsound  # Necesario para reproducir el archivo de sonido

def convertir_texto_a_voz(texto, idioma="es"):
    # Crea un objeto de audio de gTTS
    audio = gTTS(text=texto, lang=idioma, slow=False)
    
    # Guarda la audio como un archivo mp3
    audio.save("locucion.mp3")
    
    # Reproduce el archivo de sonido
    playsound("locucion.mp3")


#convertir_texto_a_voz("no andes de toxica")
