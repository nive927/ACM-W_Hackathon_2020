# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:01:20 2020

@author: Lakshmi Priya
"""

import os

# Importing module for speech conversion 
from gtts import gTTS 

# Importing module to play the converted audio 
from playsound import playsound

# Text to be converted to speech
mytext = 'Text to speech conversion successful!'

# Language
language = 'en'

# Passing the text to be converted and language to which it should be converted
# to the engine

myobj = gTTS(text=mytext, lang=language, slow=False) 

filename = "file.mp3"

# Saving the converted audio in a mp3 file
myobj.save(filename) 

# Playing the converted file 
playsound(filename)

# Delete auto file if not needed
os.remove(filename)