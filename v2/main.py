from key import *
import sys
import glob
import openai
import deepl
import subprocess
import speech_recognition as sr
from gpt import GPT

def translate(text, lang):
    try:
        result = translator.translate_text(text, target_lang=lang).text
        return result
    except:
        return ''

def say(text):
    try:
        _start = "start ./softalk/softalk.exe"
        _word = "/W:" + text.replace('\n', '')
        _command = [_start, _word]

        subprocess.run(' '.join(_command), shell=True)
        return
    
    except Exception as e:
        print("Softalk Error", e)
        return

def listen():
    print("認識中...")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ja-JP')
        if text == 'ストップ':
            subprocess.run("start ./softalk/softalk.exe /close_now", shell=True)
            sys.exit()
        
        return text
        
    except sr.UnknownValueError:
        # print("could not understand audio")
        return ''
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ''

def main():
    while True:
        text = listen()
        if text != '':
            print(text)
            prompt = translate(text, 'EN-US')
            output = translate(gpt.get_top_reply(prompt), 'JA')
            print(output)
            say(output)

if __name__ == '__main__':
    openai.api_key = key
    translator = deepl.Translator(key2)

    r = sr.Recognizer()
    mic = sr.Microphone()

    gpt = GPT(engine="text-davinci-002",
          temperature=0.5,
          max_tokens=100)

    main()
