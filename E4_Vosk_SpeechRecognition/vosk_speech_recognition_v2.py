import sys
import os
import json
from vosk import Model, KaldiRecognizer
import pyaudio

import Lexico as validador_lexico
import Sintactico as sint

# Load the Vosk model
if not os.path.exists("model"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    sys.exit(1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

# Start audio stream
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4000, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        temp_cadena = result.get("text", "")

        print("Cadena leída:", temp_cadena)
        print("Resultado léxico:", validador_lexico.procesar_cadena(temp_cadena))
        print("Sintáctico dice:", sint.valida_cadena(temp_cadena))
        print("")
