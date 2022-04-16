from googletrans import Translator

text = ''

translator = Translator()

dt = translator.detect(text)
print(dt)

translated = translator.translate(text)

print(translated.text)