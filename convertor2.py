def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('spectrogram.png')
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

#wav_file = wave.open('output.wav','rb')
#get_wav_info('output.wav')
#get_wav_info('output(1).wav')
#get_wav_info('output(2).wav')
#graph_spectrogram('output.wav')
graph_spectrogram('output(1).wav')
#graph_spectrogram('output(2).wav')