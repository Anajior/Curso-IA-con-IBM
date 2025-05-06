from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        translations = {
            'en': GoogleTranslator(source='es', target='en').translate(text),
            'fr': GoogleTranslator(source='es', target='fr').translate(text),
            'it': GoogleTranslator(source='es', target='it').translate(text),
            'de': GoogleTranslator(source='es', target='de').translate(text),
        }
        return render_template('index.html', translations=translations)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
