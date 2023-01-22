# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:01:42 2022

@author: Najoua
"""

import gtts
from playsound import playsound
# make request to google to get synthesis
tts = gtts.gTTS("Hello world")
# save the audio file
tts.save("hello.mp3")
# play the audio file
playsound("hello.mp3")
# in spanish
tts = gtts.gTTS("Hola Mundo", lang="es")
tts.save("hola.mp3")
playsound("hola.mp3")
# in spanish
# all available languages along with their IETF tag
#print(gtts.lang.tts_langs())