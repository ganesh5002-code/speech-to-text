import speech_recognition as sr
import pyttsx3 
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
        
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("???? Please speak now in English...")
        audio = recognizer.listen(source)
    
    try:
        print("???? Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

def translate_text(text, target_language="es"): 
    print("Starting translation process")
    translator = Translator()
    print("Translator object created")
    translation = translator.translate(text, dest=target_language)
    print("Translation completed")
    print(f"???? Translate text: {translation.text}")
    return translation.text

def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. French (fr)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. German (ge)")
    print("6. Italian (it)")
    print("7. Tamil (ta)")
    print("8. Russian (ru)")
    
    choice = input("Please select the target language number (1-8): ")
    language_dict = {
    "1": "hi",
    "2": "fr",
    "3": "te",
    "5": "bn",
    "5": "ge",
    "6": "it",
    "7": "ta",
    "8": "ru"
    }
    
    return language_dict.get(choice, "es")

def main():
    try:
        target_language = display_language_options()
        
        original_text = speech_to_text()
        print("After text to speech")
        if original_text:
            print("Hello")
            translated_text = translate_text(original_text, target_language=target_language)
            print("After translation")
            speak(translated_text, language="en")
            print("✅ Translation complete")
    except Exception as e:
        print("Error {e}")

if __name__ == "__main__":
    main()
    