import json
from typing import Any
import requests

def emotion_detector(text_to_analyse: str):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj: dict[str, dict[str, str]] = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)

    return response.text

    

    formatted_response: Any = json.loads(response.text)

    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return { 'label': label, 'score': score }