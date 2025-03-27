import os
from google.cloud import dialogflow


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/jhernandezch/Downloads/ivr-454802-9f525d32ccfa.json"
project_id = "ivr-454802"


session_client = dialogflow.SessionsClient()
session_path = session_client.session_path(project_id, "UN_SESSION_ID_UNICO")

# Función para obtener la respuesta de Dialogflow
def get_dialogflow_response(user_input):
    text_input = dialogflow.TextInput(text=user_input, language_code="es")  # Cambio de "en" a "es" para español
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session_path, "query_input": query_input})
    query_result = response.query_result
    return query_result.fulfillment_text


print("¡Bienvenido! ¿En qué puedo ayudarte hoy?") #Bienvenida


while True:  # Intereacción continua
    user_input = input("Tú: ")  # Obtener lo que se ingresa
    if user_input.lower() in ['salir'
                              ]:  # Terminar
        print("¡Hasta luego!")
        break
    response = get_dialogflow_response(user_input)
    print("Bot:", response)  # Repuesta