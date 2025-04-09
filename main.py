from time import sleep
import speech_recognition as sr 
# import keyboard  
import brain
import pyttsx3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask,jsonify
from flask_cors import CORS
recognizer = sr.Recognizer()
app = Flask(__name__)
CORS(app)
logs = []

BOT_NAMES = ['computador','eva']
STOP_COMMAND = 'computador pare'
listening = True 

def activate_assistant():
  global listening
  print("Estou ouvindo...")
  brain.listen()
  listening = True
#   eva title 
print('{:^30}'.format('''
      \033[1;31m
        _____                                     
   _____\    \ _______    ______    _____         
  /    / |    |\      |  |      | /      |_       
 /    /  /___/| |     /  /     /|/         \      
|    |__ |___|/ |\    \  \    |/|     /\    \     
|       \       \ \    \ |    | |    |  |    \    
|     __/ __     \|     \|    | |     \/      \   
|\    \  /  \     |\         /| |\      /\     \  
| \____\/    |    | \_______/ | | \_____\ \_____\ 
| |    |____/|     \ |     | /  | |     | |     | 
 \|____|   | |      \|_____|/    \|_____|\|_____| 
       |___|/ 
      \033[m      
                                                                                                       
'''))
print(' Entidade Virtual Altamente inteligente  ')
  
def obter_clima_google(cidade):
    # Construindo a URL de busca no Google
    query = f"tempo em {cidade}"
    url = f"https://www.google.com/search?q={query}"
    
    # Fazendo a requisição HTTP para obter o conteúdo da página
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraindo a temperatura
    try:
        temperatura = soup.find("span", {"class": "wob_t"}).text
        return temperatura
    except AttributeError:
        return None

def falar(texto):
    engine = pyttsx3.init()
    volume = 0.1
    engine.setProperty('volume', volume)
    engine.setProperty('rate', 150)  # Ajusta a velocidade da fala
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    cidade = 'Campinas'  # Substitua pela cidade 
    temperatura = obter_clima_google(cidade)
    
    hora_atual = datetime.now().time()

    # Definir os limites de horas
    manha_limite = datetime.strptime("12:00:00", "%H:%M:%S").time()
    tarde_limite = datetime.strptime("18:00:00", "%H:%M:%S").time()

    if temperatura:
        if hora_atual < manha_limite:
            mensagem = f"Bom dia Senhor, a temperatura é {temperatura} graus. O que vamos fazer hoje?"
            # print(mensagem)
            falar(mensagem)
        elif hora_atual < tarde_limite:
            mensagem = f"Boa Tarde Senhor, a temperatura é {temperatura} graus. O que vamos fazer hoje?"
            # print(mensagem)
            falar(mensagem)
        else:
            mensagem = f"Boa Noite Senhor, a temperatura é {temperatura} graus. O que vamos fazer hoje?"
            # print(mensagem)
            falar(mensagem)
    else:
        print("Não foi possível obter as informações do tempo.")
        falar("Erro no sistema, não posso notificar o tempo.")

# def record_audio():
#     global listening
#     with sr.Microphone() as source:
#         while listening:
#             audio = recognizer.listen(source, None, 3)
#             voice_data = ''

#             try:
#                 voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
#                 print(">>", voice_data)
#                 logs.append(f">> {voice_data}")  # Adiciona o log
#                 if STOP_COMMAND in voice_data:
#                     listening = False
#                     logs.append(">> Parando a escuta.")
#                     break
#                 elif any(bot_name_variation in voice_data for bot_name_variation in BOT_NAMES):
#                     activate_assistant()
#             except sr.UnknownValueError:
#                 logs.append(">> Não entendi o que você disse.")
#             except sr.RequestError:
#                 logs.append(">> Serviço offline")

def record_audio():
    global listening
    with sr.Microphone() as source:
        while listening:
            audio = recognizer.listen(source, None, 3)
            voice_data = ''

            try:
                voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
                print(">>", voice_data)
                if STOP_COMMAND in voice_data:
                    listening = False  # Parar a escuta temporariamente
                    break
                elif any(bot_name_variation in voice_data for bot_name_variation in BOT_NAMES):
                    activate_assistant()
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('Serviço offline')
                
# def activate_assistant():
#     logs.append(">> Assistente ativada.")

# @app.route('/logs')
# def get_logs():
#     print(logs)
#     return jsonify(logs)

# if __name__ == "__main__":
#     app.run(debug=True)


while True:
    record_audio()
    while not listening:
        sleep(0.05)
        with sr.Microphone() as source:  # Definindo a variável source novamente
            audio = recognizer.listen(source, None, 3)
            voice_data = ''
            try:
                voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
                print(">>", voice_data)
                if any(bot_name_variation in voice_data for bot_name_variation in BOT_NAMES):
                    activate_assistant()
                    break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('Serviço offline')
# if keyboard.is_pressed('ctrl+alt+m'):
#    Marvin.listen()
