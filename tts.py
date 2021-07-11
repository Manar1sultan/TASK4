# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:51:50 2021

@author: s7s
"""

#authenticate
url='https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/85c6dfab-83f5-4183-99d3-9b9500afc040'
apikey='351zcH9tbQ8OoU5dqr1eRg6JZXYC1sGGuvwK2oNw9H9B'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts=TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#convert a string
with open('./TTSResult.mp3','wb')as audio_file:
    res=tts.synthesize('Hello World',accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
