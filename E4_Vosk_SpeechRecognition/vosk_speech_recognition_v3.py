# reconocimiento_v3.py

import sys
import os
import json
import serial
import time
from vosk import Model, KaldiRecognizer
import pyaudio
import SintacticoConLed as sint

arduino = serial.Serial("COM3", 9600, timeout=1)  
time.sleep(2) 

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
        result = json.loads(recognizer.Result())  
        temp_cadena = result.get("text", "").strip() 
        print("Comando reconocido:", temp_cadena)

        # Verificar si es un comando válido
        if sint.valida_cadena(temp_cadena):
            print("✅ Comando válido.")
            arduino.write((temp_cadena + "\n").encode())  
        else:
            print("❌ Comando inválido.")


