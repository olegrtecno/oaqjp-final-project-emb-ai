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

    # Return the emotions dictionary in case of success
    if (response.status_code == 200):
        
        # Format the response as json
        formatted_response = json.loads(response.text)

        # Extract the emotions dictionary based on the response json structure: dictionary -> list -> dictionary
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Find the dominant emotion based on the maximum score
        dominant_emotion = max(emotions, key = emotions.get)

        # Add a new dictionary entry to indicate the dominant emotion
        emotions["dominant_emotion"] = dominant_emotion

        return emotions
    else:
        # Return the empty dictionary in case of error
        return {}