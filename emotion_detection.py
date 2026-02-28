import requests

def emotion_detector(text_to_analyze):
    """ emotion analysis using Watson NLP """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_obj= { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url, json=req_obj, headers=headers)
    return resp.text