import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj =  {"raw_document": { "text": text_to_analyse}}
    response = requests.post(url, json = obj, headers = header)
    fres = json.loads(response.text)
    output = fres["emotionPredictions"][0]["emotion"]
    output["dominant_emotion"] = max(output, key=output.get)
    return output