from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text = request.args.get("textToAnalyze", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    # sentence output str
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response_str

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
