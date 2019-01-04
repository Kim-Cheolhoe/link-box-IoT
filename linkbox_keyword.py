#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple client for GiGA Genie AI Makers Kit"""



from __future__ import print_function
from __future__ import absolute_import

import gkit
import RPi.GPIO as GPIO
import time

# set your client key information
CLIENT_ID = 'Y2xpZW50X2tleTE1MzUyNTQ0NDE3MzA='
CLIENT_KEY = 'Y2xpZW50X2lkMTUzNTI1NDQ0MTczMA=='
CLIENT_SECRET = 'Y2xpZW50X3NlY3JldDE1MzUyNTQ0NDE3MzA='

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)# GPIO Assign mode


def sample():
    point = 0
    gkit.set_clientkey(CLIENT_ID, CLIENT_KEY, CLIENT_SECRET)
    gkit.kws_start()
    gkit.kws_setkeyword('기가지니')
    while True:
        print ('========')
        point=point+1
        if gkit.kws_detect() == 200:
            stt_text = gkit.getVoice2Text()
            if point%2==1:
             GPIO.output(5,GPIO.HIGH) # out
            
            if point%2==0:
             GPIO.output(5,GPIO.LOW) # out
            
            print (stt_text)
            if stt_text != '':   
              gkit.tts_play(stt_text)

    else :
     GPIO.cleanup()

def main():

    sample()

if __name__ == '__main__':
    main()
