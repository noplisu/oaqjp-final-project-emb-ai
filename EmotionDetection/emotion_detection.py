import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=payload, headers=headers, timeout=5000)

    emotions = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
    }
    if response.status_code == 200:
        emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions
