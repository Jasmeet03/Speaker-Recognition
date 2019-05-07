import os
import numpy as np 
import sounddevice as sd 

duration = 20
sd.default.samplerate = fs 
sd.default.channels = 2 





My_Recording = sd.rec(int(duration*fs))
sd.wait()



