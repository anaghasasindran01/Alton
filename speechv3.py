from google import google
import boto3
import speech_recognition as sr
from playsound import playsound
import webbrowser
import time
import os
import random
from gtts import gTTS

#polly = session.client("polly")
#client = boto3.client('polly')



speech = sr.Recognizer() #read voice object

greeting_dict = {'hello': 'hello', 'hi': 'hi','hey':'hey'}
bye_dict = {'bye':'bye','by':'by'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
asalam_dict = {'Assalam':'Assalam','Assalamu':'Assalamu'}
python_dict = {'Run':'Run','run':'run'}

mp3_greeting_list = ['mp3/hi/hi.mp3','mp3/hi/hru.mp3','mp3/hi/wit.mp3']
mp3_bye_list = ['mp3/bye/bye.mp3','mp3/bye/byenice day.mp3','mp3/bye/havenice.mp3']
mp3_google_search = ['mp3/search1.mp3', 'mp3/search2.mp3']
va_alikum_mp3 = ['mp3/walaikkum.mp3']

python_scripts = {'forward': 'test.py'}

counter = 0

def play_sound_from_polly(result):
    global counter
    mp3_name = 'output.mp3'
    #obj = client.synthesize-speech(Text=result, OutputFormat='mp3', VoiceId='Joanna')
    tts = gTTS(text=result, lang='en')

    with open(mp3_name, 'wb') as file:
       # file.write(obj['AudioStream'].read())
       # file.close()
       tts.save(mp3_name)
    #tts = gTTS(text=result, lang='en')
    #tts.save(mp3_name)
    playsound(mp3_name)
    os.remove(mp3_name)
    counter+=1

'''
def google_search_result(query):
    search_result = google.search(query)
    for result in search_result:
        print(result.description)
        play_sound_from_polly(result.description)

google_search_result("what is earth")

exit()

'''

def google_search_result(query):
    search_result = google.search(query)

    for result in search_result:
        print(result.description.replace('-', '').rsplit('.', 3)[0])
        if result.description != '':
            play_sound_from_polly(result.description)
            break

#google_search_result("what is earth")
#exit()

def is_valid_google_search(phrase):

    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def read_voice_cmd():

    voice_text = ''
    time.sleep(1)
    playsound('mp3/litsening.mp3')
    print('Listening')

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)



    try:

        #print("You said: \n" + speech.recognize_google(audio))
        voice_text = speech.recognize_google(audio)

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network error")
    except sr.WaitTimeoutError:
        pass

    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        # 'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:

                return True
                break

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

def is_valid_notea(asalamdict, voice_note):
    for key, value in asalamdict.items():
        # 'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:

                return True
                break

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass




def is_valid_noteb(byedict, voice_note):
    for key, value in byedict.items():
        # 'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:

                return True
                break

            elif key == voice_note.split(' ')[1]:
                return False

        except IndexError:
            pass

def is_valid_notec(pythondict, voice_note):
    for key, value in pythondict.items():
        # 'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:

                return True
                break

            elif key == voice_note.split(' ')[1]:
                return False

        except IndexError:
            pass

def run_python_script(voice_note):
    script_name = voice_note.split(' ')[1]
    for key, value in python_scripts.items():
        if key == script_name:
            os.system('python {}'.format(value))



if __name__ == '__main__':


    playsound('mp3/greeting.mp3')

    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting...')
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_notea(asalam_dict, voice_note):
            print('In waalaikum...')
            play_sound(va_alikum_mp3)
            continue


        elif 'open ' in voice_note:
            print(" open folder")
            continue

        elif is_valid_noteb(bye_dict, voice_note):
            print('In bye...')
            play_sound(mp3_bye_list)
            continue

        elif is_valid_google_search(voice_note):
            print('in google search...')
            play_sound(mp3_google_search)
            #webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            google_search_result(voice_note)
            continue

        elif is_valid_notec(python_dict, voice_note):
            #print(voice_note)
            run_python_script(voice_note)
            print('run python')
            continue

        elif 'stop' in voice_note:
            print(" close")
            exit()
