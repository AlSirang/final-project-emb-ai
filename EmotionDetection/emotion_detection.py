import json
import requests

def emotion_detector(text_to_analyze):
    """ emotion analysis using Watson NLP """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_obj= { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url, json=req_obj, headers=headers)
    resp_fmt = json.loads(resp.text)
    emotions = resp_fmt['emotionPredictions'][0]['emotion']
    dominant_emotion_score=None
    dominant_emotion = None

    resp_dict = dict()

    for key,value in emotions.items():
        resp_dict[key] = value
        if dominant_emotion_score is None or dominant_emotion_score < value:
            dominant_emotion_score = value
            dominant_emotion = key
    
    resp_dict['dominant_emotion'] = dominant_emotion
        
    
    return resp_dict