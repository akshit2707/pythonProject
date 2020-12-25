import speech_recognition as sr
import pyttsx3
# import pywhatkit as py
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        command = ''
        with sr.Microphone() as source:

            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'phoenix' in command:
                command = command.replace('ploenix', '')
                print(command)

    except Exception as e:
            print(e)
    return command


def run_phoenix():
    flag = True
    while(flag):

        command = take_command()
        print(command)
        if 'hey' in command or command == 'hello':
            talk('hi user, how are you today. hope you are fine ')
        elif 'hello world' in command:
            talk('Nigga what')

        elif 'play' in command:
            try:
                song = command.replace('play', '')
                talk('playing ' + song)
                # py.playonyt(song)
            except Exception as e:
                print e
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            talk(datetime.date.today())
        elif 'day today' in command:
            now = datetime.datetime.now()
            talk(now.strftime("%A"))
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'bye' in command or 'good night' in command or 'see you' in command:
            flag = False
        elif(command==''):
            talk('Please say the command again or speak up something.')
        else:
            talk('Sorry, Akshit did not trained me for this')



run_phoenix()