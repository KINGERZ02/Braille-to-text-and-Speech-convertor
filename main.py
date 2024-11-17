import braille
import pyttsx3
#braille.textToBraille('string')
a=braille.imageToBraille('name.png')
print(a)
b=braille.imageToText('name.png')
print(b)

engine = pyttsx3.init()
engine.say(b)
engine.runAndWait()

#print hello



c=braille.brailleToTextArray('⠚⠑⠑⠞')
print(c)