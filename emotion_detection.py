# Make all necessary imports
import requests, json

# The emotion detection main implementation
def emotion_detector(text_to_analyse):

    # The Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # The API required headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # The input json for the API
    input_json = { "raw_document": { "text": text_to_analyse } }

    # The actual API call
    response = requests.post(url, json = input_json, headers = header)

    # Return the response body in case of success
    if (response.status_code == 200):
        return response.text
    else:
        return "Error occurred. Try again"