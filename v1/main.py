from key import *
import openai
import deepl
from gpt import GPT

def translate(text, lang):
    try:
        return translator.translate_text(text, target_lang=lang).text
    except:
        return ''

def main():
    while True:
        text = input()
        if text == '/stop':
            break
        prompt = translate(text, 'EN-US')
        output = translate(gpt.get_top_reply(prompt), 'JA')
        print(output)

if __name__ == '__main__':
    openai.api_key = key1
    translator = deepl.Translator(key2)

    gpt = GPT(engine="text-davinci-002",
            temperature=0.5,
            max_tokens=100)

    main()