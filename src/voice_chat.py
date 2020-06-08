import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import glob
import os


class VoiceChat():

    def __init__(self):
        # Insert API Key in place of
        # 'YOUR UNIQUE API KEY'
        authenticator = IAMAuthenticator('xGtbZTZKN1oDCuKQJXZ44zIqbbAVX0nolqQsqZyix28L')
        self.service = SpeechToTextV1(authenticator=authenticator)

        # Insert URL in place of 'API_URL'
        self.service.set_service_url(
            'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/120a01db-2718-4b07-8000-9050ed029f85')


    def translate_media_to_text(self,filepath):
        # Insert local mp3 file path in
        # place of 'LOCAL FILE PATH'

        with open(filepath,
                  'rb') as audio_file:
            dic = json.loads(
                json.dumps(
                    self.service.recognize(
                        audio=audio_file,
                        content_type='audio/mpeg',
                        model='en-US_NarrowbandModel',
                        continuous=True).get_result(), indent=2))

        # Stores the transcribed text
        text = ""

        while bool(dic.get('results')):
            text = dic.get('results').pop().get('alternatives').pop().get('transcript') + text[:]

        print(text)
        return text
