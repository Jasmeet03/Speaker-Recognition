from gtts import gTTS  
import os 


mytext = 'your practical exam is on 8th may '

 
language = 'en'

Text2Speech = gTTS(text=mytext, lang=language, slow=False) 


Text2Speech.save("welcome.mp3") 



