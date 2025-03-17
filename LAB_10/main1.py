import os
import json
import requests
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer
import webbrowser

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        model_folder = r"C:\Users\kira\Downloads\model-small-en-us-0.15"
        self.model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), model_folder)

        if not os.path.exists(self.model_path):
            print(f"Модель {self.model_path} не найдена.")
            exit(1)

        self.model = Model(self.model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

        self.current_word = None
        self.current_word_data = None

    def speak(self, text):
        print(f"Ассистент: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # Finding word function 
    def find_word_meaning(self, word):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    # Saving function in file 
    def save_word(self, word):
        with open("words.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}\n")
        self.speak(f"Слово '{word}' сохранено в файл words.txt.")

    # Actions for command
    def handle_command(self, command):
        if command.startswith("find"):
            word = command.split("find")[1].strip()
            self.current_word = word
            self.current_word_data = self.find_word_meaning(word)
            if self.current_word_data:
                self.speak(f"Слово '{word}' найдено. Что вы хотите сделать? Скажите 'meaning', 'link' или 'save'.")
            else:
                self.speak(f"Извините, я не смог найти слово '{word}'.")
        elif command == "meaning":
            if self.current_word_data:
                meanings = self.current_word_data[0]['meanings']
                for meaning in meanings:
                    part_of_speech = meaning['partOfSpeech']
                    definition = meaning['definitions'][0]['definition']
                    self.speak(f"{self.current_word} ({part_of_speech}): {definition}")
            else:
                self.speak("Сначала найдите слово с помощью команды 'find <слово>'.")
        elif command == "link":
            if self.current_word:
                url = f"https://dictionary.cambridge.org/dictionary/english/{self.current_word}"
                webbrowser.open(url)
                self.speak(f"Открываю ссылку на слово '{self.current_word}' в браузере.")
            else:
                self.speak("Сначала найдите слово с помощью команды 'find <слово>'.")
        elif command == "save":
            if self.current_word:
                self.save_word(self.current_word)
            else:
                self.speak("Сначала найдите слово с помощью команды 'find <слово>'.")
        elif command == "example":
            self.speak("Пример использования команды: 'find apple'.")
        elif command == "exit":
            self.speak("Выключаюсь. До свидания!")
            exit()
        else:
            self.speak("Извините, я не понял команду.")

    # Main assistant loop
    def run(self):
        self.speak("Привет! Я ваш голосовой ассистент. Как я могу помочь?")
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                result_dict = json.loads(result)
                command = result_dict.get("text", "").lower()
                print(f"Вы сказали: {command}")
                if command:
                    self.handle_command(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()