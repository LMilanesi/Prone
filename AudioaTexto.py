from pydub import AudioSegment
import speech_recognition as sr

# Ruta del archivo de origen y destino
input_ogg_path = r'C:\Users\Lauta\OneDrive\Escritorio\Prone\WhatsApp Ptt 2024-08-14 at 13.05.42.ogg'
output_wav_path = r'C:\Users\Lauta\OneDrive\Escritorio\Prone\WhatsApp Ptt 2024-08-14 at 13.05.42.wav'

# Convertir de OGG a WAV
audio = AudioSegment.from_ogg(input_ogg_path)
audio.export(output_wav_path, format='wav')

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Leer el archivo WAV y convertir a texto
with sr.AudioFile(output_wav_path) as source:
    audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, language="es-ES")

# Imprimir el texto resultante
print(text)