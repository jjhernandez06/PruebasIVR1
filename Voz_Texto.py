import pyttsx3

continuar = 'Si'

motor = pyttsx3.init()  #Se iniacializa el motor
motor.setProperty('rate', 150)  # Cambiar velocidad de voz
motor.setProperty('volume', 1)  # Volumen (de 0 a 1)

while continuar == 'Si':

    texto = input("Escribe el texto que a convertir: ") # Texto para convertir a voz
    

    motor.say(texto) # Se convierte el texto a voz
    motor.runAndWait() # Se ejecuta la voz
    continuar = input("Deseas continuar? Si/No: ")
    exit()
   

   