import requests  # Import the requests library to handle HTTP requests
import json 

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    if response.status_code ==  400:
        error_output = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
        return error_output
    else:
        formatted_response = json.loads(response.text)

        scores = formatted_response["emotionPredictions"][0]["emotion"]
        predicted_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = predicted_emotion
        return scores  # Return the response text from the API