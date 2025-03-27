import os
import speech_recognition as rs
import pyttsx3
import pyaudio
#from google.cloud import dialogflow_v2 as dialogflow
from google.cloud import dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "C:/Users/jhernandezch/Downloads/ivr-454802-9f525d32ccfa.json"
project_id ="ivr-454802"

session_client = dialogflow.SessionsClient()
session_path = session_client.session_path(project_id,"UN_SESSION_ID_UNICO")

reconocedor = rs.Recognizer()

with rs.Microphone() as mic: #Mic captura audio
    try:
       
        reconocedor.adjust_for_ambient_noise(mic, duration=0.2) # Ajuste para ruido mejor audio
        audio = reconocedor.listen(mic) #Se captura el audio
        texto = reconocedor.recognize_google(audio) # Se reconoce la voz usando Google
        texto = texto.lower()

        
        print("Estas son tus palabras -->", texto) # Mostrar el texto que se reconocio

    except rs.UnknownValueError:
        print("No se pudo entender el audio.")   # Si no se puede entender el audio
    except rs.RequestError as e:
        
        print(f"Error en los| resultados desde Google Speech Recognition; {e}") # Si haya un error al hacer la solicitud a Google


text_input = dialogflow.TextInput(text=texto, language_code="en")
query_input = dialogflow.QueryInput(text=text_input)
response = session_client.detect_intent(request={"session": session_path, "query_input": query_input})
query_result = response.query_result
print("Respuesta:", query_result.fulfillment_text)





#continuar = 'Si'

motor = pyttsx3.init()  #Se iniacializa el motor
motor.setProperty('rate', 150)  # Cambiar velocidad de voz
motor.setProperty('volume', 1)  # Volumen (de 0 a 1)

#while continuar == 'Si':

   # texto1 = input("Escribe el texto que a convertir: ") # Texto para convertir a voz
    
#texto1 = input(query_result.fulfillment_text)
motor.say(query_result.fulfillment_text) # Se convierte el texto a voz
motor.runAndWait() # Se ejecuta la voz
  #  continuar = input("Deseas continuar? Si/No: ")
    #exit()