import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')


def translator_instance(text, model):
    """
    text: String you want to translate
    mode: String of model name for example 'en-es' if you want
          to translate from english to spanish
    """
    translation = language_translator.translate(
        text=text,
        model_id=model).get_result()
    return(json.dumps(translation, indent=2, ensure_ascii=False))

def englishToFrench(text):
    #write the code here
    translator_instance(text, "en-fr")
    return frenchText

def englishToFrench(text):
    translator_instance(text, "fr-en")
    return englishText