import os
from gtts import gTTS

Text = "Hi,i am anamul bhuyan. i am love python language. i also love django framework also"
print("Please wait...processing")
TTS = gTTS(text=Text,lang='en-uk')

TTS.save("voice.mp3")
os.system("start voice.mp3")

# txt = "almin"
# print("wait....processing is running")
# t = gTTS(text=txt,lang='en-us')
# t.save('voice.mp3')
# os.system('start voice.mp3')