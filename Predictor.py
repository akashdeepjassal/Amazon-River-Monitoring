import keras
import numpy as np
import cv2
import pandas as pd
import h5py
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from keras.models import load_model

def val2labels(pred):
    if(pred=='16'):
        predf='primary'
        return(predf)
    if(pred=='15'):
        predf='cultivation'
        return(predf)
    if(pred=='14'):
        predf='haze'
        return(predf)
    if(pred=='13'):
        predf='artisinal_mine'
        return(predf)
    if(pred=='12'):
        predf='clear'
        return(predf)
    if(pred=='11'):
        predf='cloudy'
        return(predf)
    if(pred=='10'):
        predf='agriculture'
        return(predf)
    if(pred=='9'):
        predf='blow_down'
        return(predf)
    if(pred=='8'):
        predf='partly_cloudy'
        return(predf)
    if(pred=='7'):
        predf='water'
        return(predf)
    if(pred=='6'):
        predf='habitation'
        return(predf)
    if(pred=='5'):
        predf='slash_burn'
        return(predf)
    if(pred=='4'):
        predf='selective_logging'
        return(predf)
    if(pred=='3'):
        predf='blooming'
        return(predf)
    if(pred=='2'):
        predf='road'
        return(predf)
    if(pred=='1'):
        predf='bare_ground'
        return(predf)
    if(pred=='0'):
        predf='conventional_mine'
        return(predf)
input_size = 64
input_channels = 3
learning_rate = 0.01
lr_decay = 1e-1
tags={
        0: 'conventional_mine',
        1: 'bare_ground',
        2: 'road',
        3: 'blooming',
        4: 'selective_logging',
        5: 'slash_burn',
        6: 'habitation',
        7: 'water',
        8: 'partly_cloudy',
        9: 'blow_down',
        10: 'agriculture',
        11: 'cloudy',
        12: 'clear',
        13: 'artisinal_mine',
        14: 'haze',
        15: 'cultivation',
        16: 'primary'
        }
variable_image=str(input())
x_test=[]
img1=cv2.imread('input/test-jpg/'+'test_' + variable_image
                 +'.jpg')
#cv2.imshow('image',img)
img = cv2.resize(img1,(input_size, input_size))
x_test.append(img)
x_test = np.array(x_test, np.float32)

fname='weights.h5'
# load weights from first model; will only affect the first layer, dense_1.
model=load_model(fname)
opt = Adam(lr=learning_rate, decay=lr_decay)

model.compile(loss='binary_crossentropy',
              # We NEED binary here, since categorical_crossentropy l1 norms the output before calculating loss.
              optimizer=opt,
              metrics=['accuracy'])
preds=model.predict(x_test)
pred=model.predict_classes(x_test)
#print(preds)
#print('{}'.format(pred))
font = cv2.FONT_HERSHEY_SIMPLEX
#preds=str(preds)
pred=str(pred)
pred=pred.strip('[')
pred=pred.strip(']')
#print('{}'.format(pred))
#print('{}'.format(str(pred)))
#print(tags.keys())
predf=str(val2labels(pred))
print("{} {}".format(pred,predf))
cv2.putText(img1,predf,(0,130), font, 1, (255,255,155), 2, cv2.LINE_AA)
cv2.imshow('image',img1)
#Display the image
cv2.waitKey(0)
cv2.destroyAllWindows()
