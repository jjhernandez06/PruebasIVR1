import os
from google.cloud import dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "C:/Users/jhernandezch/Downloads/ivr-454802-9f525d32ccfa.json"
project_id ="ivr-454802"

session_client = dialogflow.SessionsClient()
session_path = session_client.session_path(project_id,"UN_SESSION_ID_UNICO")

text_input = dialogflow.TextInput(text="Hola el correo personal", language_code="en")
query_input = dialogflow.QueryInput(text=text_input)
response = session_client.detect_intent(request={"session": session_path, "query_input": query_input})
query_result = response.query_result
print("Respuesta:", query_result.fulfillment_text)