import parselmouth

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd 
import csv 

sns.set()

def Loader():
    i = -1
    rootdir = "/home/jasmeet/Desktop/cs project/audio"
    for subdir ,dirs , files in os.walk(rootdir):
        os.chdir(subdir)
        for file in files:
            if file.endswith('wav'):
                i = i+1
                try:
                    snd = parselmouth.Sound(subdir+'/'+file)
                    '''
                    sp = subdir.split('/')[-1]
                    if (sp == 'Anny'):
                        a = 'female'
                    elif (sp == 'Neha'):
                        a = 'Female'
                    else:
                        a = 'Male'
                    '''
                    intensity = snd.to_intensity()
                    pitch = snd.to_pitch()
                    pre_emphasized_snd = snd.copy()
                    pre_emphasized_snd.pre_emphasize()
                    spectrogram = pre_emphasized_snd.to_spectrogram(window_length=0.03, maximum_frequency=8000)
                    draw_spectrogram(spectrogram)
                    draw_pitch(pitch)

                except:
                    continue
def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    
def draw_intensity(intensity):
    	plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    	plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    	plt.grid(False)
    	plt.ylim(0)
    	plt.ylabel("intensity [dB]")

def draw_pitch(pitch):
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    #print(pitch_values)
    with open ('person.csv','a  n  ') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows([pitch_values])
        csvFile.flush()
    csvFile.close




    #print (pitch_values)

Loader()
