import os

import speech_recognition as rs
import pyaudio
from google.cloud import dialogflow_v2 as dialogflow

reconocedor = rs.Recognizer()
while True: # inicia el ciclo
 with rs.Microphone() as mic: #Mic captura audio
    try:
       
        reconocedor.adjust_for_ambient_noise(mic, duration=0.2) # Ajuste para ruido mejor audio
        print("Hable ahora")
        audio = reconocedor.listen(mic) #Se captura el audio
        texto = reconocedor.recognize_google(audio) # Se reconoce la voz usando Google
        texto = texto.lower()

        
        print("Estas son tus palabras -->", texto) # Mostrar el texto que se reconocio
        break

    except rs.UnknownValueError:
        print("No se pudo entender el audio. Hable de nuevo.")   # Si no se puede entender el audio pedira hablar nuevamente
    except rs.RequestError as e:
        
        print(f"Error en los| resultados desde Google Speech Recognition; {e}") # Si haya un error al hacer la solicitud a Google

