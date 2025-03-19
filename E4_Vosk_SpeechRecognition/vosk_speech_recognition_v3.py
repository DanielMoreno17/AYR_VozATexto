# reconocimiento_v3.py
import sys
import os
from vosk import Model, KaldiRecognizer
import Lexico as validador_lexico
import pyaudio
import SintacticoConLed
import json

if not os.path.exists("model"):
    print("Por favor, descarga el modelo desde https://alphacephei.com/vosk/models y descomprímelo como 'model'.")
    sys.exit(1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("🎤 Escuchando...")

while True:
    data = stream.read(4000)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())  
        temp_cadena = result.get("text", "")  

        print("Cadena leída:", temp_cadena)
        print("Resultado léxico:", validador_lexico.procesar_cadena(temp_cadena))

        if SintacticoConLed.valida_cadena(temp_cadena):
            print("✅ Comando válido.")
        else:
            print("❌ Comando inválido.")
