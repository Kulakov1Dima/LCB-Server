import os
import uvicorn
import subprocess
from fastapi import Body, FastAPI, WebSocket

app = FastAPI()

@app.get("/", tags=["Home"], summary="Главная страница сервера")
def home():
    return "hello"

@app.post("/", tags=["Alice Bot"], summary="Навык Яндекс Алисы")
def read_Alice(request = Body(embed=True), session = Body(embed=True)):
    if(session['message_id'] == 0):
        results = {
            "response": {
                "text": "Здравствуйте, для данной игры нужно двое. Я помогу вам в управлении вашей светодиодной шахматной доской, доступные команды: помощь, что ты умеешь делать? Перезагрузи игру. Для выхода из навыка скажите хватит.",
                "tts": "Здр+авствуйте, для д+анной игры нужно двое. Я помог+у вам в управл+ении в+ашей светоди+одной ш+ахматной доск+ой, доступные команды: помощь, что ты умеешь делать? Перезагрузи игру. Для выхода из навыка скажите хватит."
            },
            "version": "1.0"
        }
    else:
        if(request['command'] == "помощь"):
            results = {
                "response": {
                    "text": "ты говно.",
                    "tts": "ты говн+о."
                },
                "version": "1.0"
            }
        else:
            results = {
                "response": {
                    "text": request['command']
                },
                "version": "1.0"
            }
    return results

def transliterate_russian_to_english(text):
    # Словарь для замены символов
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
        'Я': 'Ya'
    }

    # Транслитерируем текст
    transliterated_text = ''.join(translit_dict.get(char, char) for char in text)

    return transliterated_text

@app.get("/data")
def getData():
    with open("kal.txt", "r", encoding="utf-8") as file:
        content = file.read()
        transcribed_content = transliterate_russian_to_english(content)  # транслитерация с русского на английский
        return transcribed_content

def run_servers():
    http_server = subprocess.Popen(["python3", "-m", "uvicorn", "main:app", "--host", "192.168.0.48", "--port", "80", "--reload"])
    https_server = subprocess.Popen(["python3", "-m", "uvicorn", "main:app", "--host", "192.168.0.48", "--port", "443", "--reload", "--ssl-keyfile", "checkers.key", "--ssl-certfile", "checkers.crt"])
    
    # Ожидание завершения обоих процессов
    http_server.communicate()
    https_server.communicate()

if __name__ == "__main__":
    run_servers()
    #uvicorn.run("main:app", host="localhost", port=80, reload=True)#192.168.0.48