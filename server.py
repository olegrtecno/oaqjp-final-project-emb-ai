''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the detected emotions
        along with their scores, as well as the dominant emotion
        for the provided text.
    '''
    # Retrieve the user provided text
    text_to_analyze = request.args.get('textToAnalyze')

    # Run the emotion detector fundion
    response = emotion_detector(text_to_analyze)

    # Initial displayed response string
    response_string = "For the given statement, the system response is "

    # Go over all emotions detected and add them to the response
    keys = list(response.keys())
    for i in range(len(response)):
        # The dominant emotion is added at the end
        if keys[i] != "dominant_emotion":
            # While haven't reached the last emotion
            if i < (len(response)-2):
                response_string += f'\'{keys[i]}\': {response[keys[i]]}, '
            # Last emotion
            else:
                # Remove the last comma and space characters first
                response_string = response_string[:-2]
                response_string += f' and \'{keys[i]}\': {response[keys[i]]}. '
        else:
            # Now add the dominant emotion indication
            dominant_emotion = response[keys[i]]
            if dominant_emotion is None:
                response_string = "Invalid text! Please try again!"
            else:
                response_string += f'The dominant emotion is {dominant_emotion}.'

    return response_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
