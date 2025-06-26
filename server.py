"""Flask Server file to run app to analyze text on IBM Watson NLP Library."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Index URL route"""
    return render_template('index.html')

@app.route("/emotionDetector")
def get_emotion_detection_result():
    """Evalutation of String in input, will be displayed in result_string format."""
    result_score = emotion_detector(request.args.get('textToAnalyze'))
    if 'dominant_emotion' in result_score:
        if result_score['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
        anger = result_score['anger']
        disgust = result_score['disgust']
        fear = result_score['fear']
        joy = result_score['joy']
        sadness = result_score['sadness']
        dominant = result_score['dominant_emotion']
        result_string = f"For the given statement, the system response is 'anger': {anger}, " \
                        f"'disgust': {disgust}, 'fear': {fear}, " \
                        f"'joy': {joy} and 'sadness': {sadness}. " \
                        f"The dominant emotion is <b>{dominant}</b>"
        return result_string
    return "Dominant emotion missing, something might be wrong in code."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
