"""This is the module docstring"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_func():
    """Emotion Detector"""

    text_to_analyse = request.args.get('textToAnalyze')
    emotion_output = emotion_detector(text_to_analyse)

    if emotion_output['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    emotion_text_output = (
    f"For the given statement, the system response is "
    f"'anger': {emotion_output['anger']}, 'disgust': {emotion_output['disgust']}, "
    f"'fear': {emotion_output['fear']}, 'joy': {emotion_output['joy']} \
     and 'sadness': {emotion_output['sadness']}. "
    f"The dominant emotion is {emotion_output['dominant_emotion']}."
    )

    return emotion_text_output

@app.route("/")
def render_index_page():
    """render Index Page Template"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)
