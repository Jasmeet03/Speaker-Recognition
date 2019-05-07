import  cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GMM
#import sklearn.mixture.gaussian_mixture as GMM
from featureextraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

#path to training data
# source   = "development_set/"
#source   = "/home/jasmeet/Desktop/cs project/audio/"   

#path where training speakers will be saved

# dest = "speaker_models/"
# train_file = "development_set_enroll.txt"

dest = "/home/jasmeet/Desktop/cs project/Speakers_models/"
train_file = "/home/jasmeet/Desktop/cs project/trainingdata.txt"        
file_paths = open(train_file,'r')

count = 0
# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print (path)
    
    # read the audio
    sr,audio = read(path)
    
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 5 files of speaker are concatenated, then do model training
	# -> if count == 5: --> edited below
    if count == 9:    
        gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("/")[-2]+".gmm"
        print(picklefile)
        cPickle.dump(gmm,open(dest + picklefile,'wb'))
        print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)    
        features = np.asarray(())
        count = -1
    count = count + 1