from sklearn.utils import shuffle
import os

import numpy as np
import tensorflow as tf
import gc



def MCNN_data_load():

   

    path_data_training =  "../dataset/train/data.npy"
    path_label_training ="../dataset/train/label.npy"
    
    path_data_testing = "../dataset/test/data.npy"
    path_label_testing = "../dataset/test/label.npy"
    
    path_data_antiporter = "../dataset/antiporter/data.npy"
    path_label_antiporter = "../dataset/antiporter/label.npy"

    
    x_train,y_train=data_load(path_data_training,path_label_training)
    
    x_test,y_test=data_load(path_data_testing,path_label_testing)
    
    x_antiporter,y_antiporter=data_load(path_data_antiporter,path_label_antiporter)
    
    return(x_train,y_train,x_test,y_test,x_antiporter,y_antiporter)

def data_load(DATA,LABEL):
    data=np.load(DATA)
    label=np.load(LABEL)
    x=data
    y= tf.keras.utils.to_categorical(label,2)
    gc.collect()
    return x ,y