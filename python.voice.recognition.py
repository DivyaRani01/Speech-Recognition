import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)  # Print the available voices and their indices
engine.setProperty('voice', voices[0].id)  # Modify the index accordingly

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""  # Initialize command with an empty string
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aish' in command:
                command = command.replace('patthan', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say the command again.")
    except sr.RequestError:
        print("Sorry, I'm unable to process your request. Please try again later.")
    return command

def run_Aish():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry, I didn't understand that. Please say the command again.")

while True:
    run_Aish()
