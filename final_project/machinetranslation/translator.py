
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('KKWAvRAETCYISIsyfeQxnHWi1sBCdY81T4SyK3mfu8S8')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/43a42fd1-6cc8-4609-8f6f-0e1fed1b4ce4')

def english_to_french(english_text):
    '''Translation of english to french'''
    french_translation=language_translator.translate(
        text=english_text,model_id='en-fr').get_result()
    french_text=french_translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Translation of french to english'''
    eng_translation=language_translator.translate(
        text=french_text,model_id='fr-en').get_result()
    english_text=eng_translation['translations'][0]['translation']
    return english_text
