from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)
    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {resp['anger']}, 'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
