# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

import requests
import json

def emotion_detector(text):
    text_to_analyze = text

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_dict = { "raw_document": { "text": text_to_analyze } }
    # sending the post request with the info above
    response = requests.post(url, json=input_dict, headers=headers, verify=True)
    if response.status_code == 400 or response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    response.raise_for_status()
    # converting the output text into json format
    json_response = json.loads(response.text)
    # extracting only the list of emotions, which is the first dict of first element
    
    emotions_output = json_response['emotionPredictions'][0]['emotion']
    
    dominant_emotion = max(emotions_output, key=emotions_output.get)# extracting the emotion with the highest score
    emotions_output.update({'dominant_emotion': dominant_emotion}) # adding the donminant to the output dictionary
    return emotions_output