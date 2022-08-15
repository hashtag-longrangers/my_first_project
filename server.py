import json
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def English_To_French():
    textToTranslate = request.args.get('textToTranslate')
    French_Translation_Text = translator.English_to_French(textToTranslate)
    return  French_Translation_Text

@app.route("/frenchToEnglish")
def French_To_English():
    textToTranslate = request.args.get('textToTranslate')
    English_Translation_Text = translator.French_to_English(textToTranslate)
    return English_Translation_Text

@app.route("/")
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
