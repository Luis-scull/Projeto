import pyttsx3
import speech_recognition as sr

# Inicializando o motor de síntese de voz
engine = pyttsx3.init()

# Função para falar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para ouvir e reconhecer o que foi dito
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Reconhecendo...")
        text = recognizer.recognize_google(audio, language='pt-BR')
        return text.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Não foi possível acessar o serviço de reconhecimento de fala.")
        return ""

# Função para responder a perguntas
def assistant():
    speak("Olá! Sou sua assistente virtual. Em que posso ajudar?")
    
    while True:
        user_input = listen()
        
        if "parar" in user_input:
            speak("Até logo!")
            break
        
        # Adicione mais comandos aqui
        if "como você está" in user_input:
            speak("Estou bem, obrigada por perguntar!")
        elif "qual é o seu nome" in user_input:
            speak("Meu nome é assistente virtual.")
        else:
            speak("Desculpe, não entendi. Pode repetir?")
            
if __name__ == "__main__":
    assistant()
