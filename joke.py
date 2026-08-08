import speech_recognition as sr
import pyttsx3
import random

current_rate = 150
current_volume = 1.0

def samples():
    return [
        "Welcome to the future of AI voice control!",
        "I am running completely offline on your computer.",
        "Did you know Python is named after Monty Python?",
        "Systems are fully operational and ready for your command.",
        "Let's write some amazing code together today!",
        "Coding is the closest thing we have to real magic."
    ]

def jokes():
    return [
        "Why do programmers wear glasses? Because they can't C#.",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Why did the functions stop arguing? They didn't want to raise an exception.",
        "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'"
    ]

def speak(text):
    global current_rate, current_volume
    engine = pyttsx3.init()
    engine.setProperty('rate', current_rate)
    engine.setProperty('volume', current_volume)
    
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Please speak your command now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
        
    try:
        print("⚡ Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text.lower().strip()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
        return ""

def process_command(command):
    global current_rate, current_volume

    if not command:
        fallback_msg = "I didn't quite catch that. Try again!"
        print(f"❌ {fallback_msg}")
        speak(fallback_msg)
        return

    if "speed up" in command:
        current_rate += 40
        msg = f"Increasing speech speed to {current_rate} words per minute."
        print(msg)
        speak(msg)
        
    elif "slow down" in command:
        current_rate = max(70, current_rate - 40)  # Lower safety floor
        msg = f"Decreasing speech speed to {current_rate} words per minute."
        print(msg)
        speak(msg)

    elif "increase volume" in command:
        current_volume = min(1.0, current_volume + 0.2)
        msg = f"Volume increased to {int(current_volume * 100)} percent."
        print(msg)
        speak(msg)
        
    elif "decrease volume" in command:
        current_volume = max(0.1, current_volume - 0.2)  # Upper safety floor
        msg = f"Volume decreased to {int(current_volume * 100)} percent."
        print(msg)
        speak(msg)

    # Assignment Requirement 3: Custom Joke Command
    elif "tell a joke" in command:
        joke = random.choice(jokes())
        print(f"🤖 Joke: {joke}")
        speak(joke)

    # Alternate baseline task feature: Read custom sample phrases
    elif "read phrases" in command or "sample phrase" in command:
        phrase = random.choice(samples())
        print(f"📢 Sample Phrase: {phrase}")
        speak(phrase)

    # Assignment Requirement 4: Unrecognized Input Fallback Routine
    else:
        fallback_msg = "I didn't quite catch that. Try again!"
        print(f"❌ {fallback_msg}")
        speak(fallback_msg)

def main():
    print("="*20)
    print("  VOICE MASTER+: EXTEND YOUR TALKING AI       ")
    print("="*20)
    print("Available Commands:")
    print("'tell a joke' ->'read phrases'")
    print("'speed up' -> 'slow down'")
    print("'increase volume' -> 'decrease volume'")
    print("'exit' -> (stops the application)")
    print("="*20)

    while True:
        try:
            command = speech_to_text()
            if "exit" in command:
                goodbye_text = "Shutting down Voice Master application. Goodbye!"
                print(f"\n👋 {goodbye_text}")
                speak(goodbye_text)
                break
            process_command(command)
            
        except KeyboardInterrupt:
            print("\n👋 Process interrupted manually. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
