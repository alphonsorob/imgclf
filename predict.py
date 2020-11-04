#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('model1.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)


        if result[0][0] == 1:
            prediction = 'earth'
            return [{ "image" : prediction}]
        elif result[0][1] == 1:
            prediction = 'jupiter'
            return [{ "image" : prediction}]
        elif result[0][2] == 1:
            prediction = 'mars'
            return [{ "image" : prediction}]
        elif result[0][3] == 1:
            prediction = 'saturn'
            return [{ "image" : prediction}]
