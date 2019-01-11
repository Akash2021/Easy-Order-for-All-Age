from flask import Flask, render_template, request
import numpy as np
import os
from webpage.predict import get_tensor, get_prediction

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def upload_file():
    # if request.method == 'GET':
    #     return render_template('index.html', value='please,upload your face image.')
    if request.method == 'POST':
        age = 50
        prob = 0.0
        if 'file' not in request.files:
            print("file not uploaded")
            return render_template('index.html', value='please,upload your face image.')
        file = request.files['file']
        image = file.read()
        tensor = get_tensor(image)
        prob, age = get_prediction(tensor)
        text = 'I guess you are {0} years old. I\"m {1:3.1f}% sure'.format(age, prob)
        return render_template('index.html', fontsize=age+20, button_size=age-15, result=text)
    return render_template('index.html', value='please,upload your face image.')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000))
