import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Now the time is ' + time)
    elif 'date today' in command:
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        print(date)
        talk('Date today is ' + date)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'Say something about' in command:
        person1 = command.replace('Say something about', '')
        info = wikipedia.summary(person1, 1)
        print(info)
        talk(info)
    elif 'How are you' in command:
        talk('Thanks for asking me. I am good')
        print('Thanks for asking me. I am good.')
    elif 'favour' in command:
        talk('Yeah! Sure. What can I do for you')
        print('Yeah! Sure. What can I do for you')
    else:
        talk('Please come again')
        print('Please come again')


def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening.. Say something..')
            voice = listener.listen(source)
            print('heard your voice..')
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print("You said : {}".format(command))
    except:
        pass
    return command


while True:
    run_alexa()
