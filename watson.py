import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions, EmotionOptions, RelationsOptions, SemanticRolesOptions, SentimentOptions, SyntaxOptions

from ibm_watson import ToneAnalyzerV3


'''
DATA MODEL

resonse = {
   "usage":{},
   "sentiment":{},
   "semantic_roles":[],
   "relations":[
      {},
      {},
      {}
   ],
   "language":"en",
   "keywords":[
      {},
      {}
   ],
   "entities":[
      {},
      {}
   ],
   "emotion":{},
   "concepts":[],
   "categories":[],
   "warnings":[]
}


'''



# NLU
def nluLogin():
   nlu_apiKey = ''
   nlu_url = ''
   authenticator = IAMAuthenticator(f'{nlu_apiKey}')
   natural_language_understanding = NaturalLanguageUnderstandingV1(
      version='2020-08-01',
      authenticator=authenticator)
   natural_language_understanding.set_service_url(f'{nlu_url}')
   return natural_language_understanding
def natural_language_understanding_CLIENT( natural_language_understanding , text):
   response = natural_language_understanding.analyze(
         text=text,
         features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=100),
            keywords=KeywordsOptions(emotion=True, sentiment=True, limit=100),
            categories=CategoriesOptions(limit=100),
            concepts=ConceptsOptions(limit=100),
            emotion=EmotionOptions(),
            relations=RelationsOptions(),
            semantic_roles=SemanticRolesOptions(),
            sentiment=SentimentOptions(),
            syntax=SyntaxOptions(),
            )
      ).get_result()
   return json.dumps(response, indent=2)



# TONE
def toneLogin():
   tone_apiKey = 'MvAq0o5IfxSDwLCKDi9QwNKWNiUpwqoJibS4RjiCw2Nq'
   tone_url = ''

   authenticator = IAMAuthenticator(f'{tone_apiKey}')
   tone_ai = ToneAnalyzerV3(
      version='2017-09-21',
      authenticator=authenticator
   )
   tone_ai.set_service_url(tone_url)
   return tone_ai
def tone_CLIENT(tone_ai , text):
   result = tone_ai.tone(text).get_result()
   return json.dumps(result, indent=2)










# calling functions down here


# tone
tone_ai = toneLogin()
tone = tone_CLIENT(tone_ai , 'lyrics'  )
print(tone)


# sentiment
nlu_Login = nluLogin()
nlu = natural_language_understanding_CLIENT( nlu_Login,  'im so sad!'  )
print(nlu)

