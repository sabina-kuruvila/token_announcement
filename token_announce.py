from gtts import gTTS
from playsound import playsound

# Input token number
token = input("Enter the token number: ")

# Prepare the text to be spoken
txt = "ടോക്കൺ നമ്പർ  " + token

# convert the text to speech in malayalam
ob = gTTS(txt, lang='ml')

# save the speech as an MP3 file
ob.save("token.mp3")

#play the sound
playsound("token.mp3")