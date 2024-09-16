"""Module for emotion detection using Flask."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder="templates")

@app.route("/")
def render_index():
    """Render the index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emo_det():
    """Detect emotions from the provided text."""
    text_to_analyze = request.args.get("textToAnalyze")  # getting what the user has entered
    output_dict = emotion_detector(text_to_analyze)  # executing emotion_detector function

    # getting the values to format:
    anger = output_dict['anger']
    disgust = output_dict['disgust']
    fear = output_dict['fear']
    joy = output_dict['joy']
    sadness = output_dict['sadness']
    dominant_emotion = output_dict['dominant_emotion']

    # performing the format:
    formatted_string = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    if dominant_emotion is None:  # Changed comparison to 'is None'
        return "Invalid text! Please try again!"

    return formatted_string
