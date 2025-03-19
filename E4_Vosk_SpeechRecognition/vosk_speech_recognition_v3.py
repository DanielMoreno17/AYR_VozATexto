# reconocimiento.py
import sys
import os
from vosk import Model, KaldiRecognizer
import Lexico as validador_lexico
import pyaudio
import SintacticoConLed
import json

# Carga el modelo de Vosk
if not os.path.exists("model"):
    print("Por favor, descarga el modelo desde https://alphacephei.com/vosk/models y descomprímelo como 'model'.")
    sys.exit(1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

# Inicia el micrófono
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("🎤 Escuchando...")

while True:
    data = stream.read(4000)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())  # Convertir JSON a diccionario
        temp_cadena = result.get("text", "")  # Ahora sí puedes usar .get()

        print("Cadena leída:", temp_cadena)
        print("Resultado léxico:", validador_lexico.procesar_cadena(temp_cadena))

        if SintacticoConLed.valida_cadena(temp_cadena):
            print("✅ Comando válido.")
            # Aquí puedes enviar el comando a Arduino
        else:
            print("❌ Comando inválido.")
