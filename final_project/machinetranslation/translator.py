"""
high level support for doing this and that.
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def translator_instance(text, model):
    """
    text: String you want to translate
    mode: String of model name for example 'en-es' if you want
          to translate from english to spanish
    """
    translation = language_translator.translate(
        text=text,
        model_id=model).get_result()
    return json.dumps(translation, indent=2, ensure_ascii=False)

def english_to_french(text):
    """
    Translated the English text to French
    """
    #write the code here
    french_text = translator_instance(text, "en-fr")
    return french_text

def french_to_english(text):
    """
    Translated the French text to English
    """
    english_text = translator_instance(text, "fr-en")
    return english_text
