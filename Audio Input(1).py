import pyaudio
import wave
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
'''

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("Recording...")
print("Please Reapeat the following Lines")
print("hello Program")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished!")

stream.stop_stream()
stream.close()
p.terminate()

'''
 
def Recorder(WAVE_OUTPUT_FILENAME , CHANNELS , FORMAT , RATE ):

	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
        	        channels=CHANNELS,
        	        rate=RATE,
        	        input=True,
        	        frames_per_buffer=CHUNK)
	print("Recording...")
	print("Please Reapeat the following Lines")
	print("hello Program")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		    data = stream.read(CHUNK)
		    frames.append(data)

	print("Recording finished!")

	stream.stop_stream()
	stream.close()
	p.terminate()


	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def Caller ():
	a = input("Enter your Name")
	os.mkdir(a)
	os.chdir(a)
	for i in range (5):
		b =  (a + str(i) + '.wav')
		Recorder(b , CHANNELS = 2 , FORMAT = pyaudio.paInt16 , RATE = 44100)

Caller()
