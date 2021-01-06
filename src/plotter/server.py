import flask, os
import numpy as np
import tensorflow as tf

from flask import request, send_file, jsonify
from recurrence_plot import RecurrencePlot as rp

from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from PIL import Image

app = flask.Flask(__name__)
app.config['DEBUG'] = True

path = os.path.dirname(os.path.realpath(__file__))

def get_model():
    global model
    model = load_model('jupyter/models/recurrence_plot_model.h5')
    print(' * Model loaded!')


def preprocess_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image

get_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    im = Image.open('plotpic.png')

    processed_image = preprocess_image(im, target_size=(224, 224))
    prediction = model.predict(processed_image).tolist()

    print(prediction)

    response = {
        'prediction':{
            'chaotic':prediction[0][0],
            'periodic':prediction[0][1],
            'trend':prediction[0][2]
        }
    }

    return jsonify(response)



@app.route('/plot_json/', methods=['POST'])
def plot_json():
    body = request.json
    data_floats = [float(i) for i in body['data']]

    M, N, compareMode = body['M'], body['N'], body['compareMode']

    rec_plot = rp(M, N, data_floats, compareMode)
    rec_plot.draw_diagram()

    return {
        'plot_data': rec_plot.similarities
    }


@app.route('/plot_image/', methods=['POST'])
def plot_image():
    body = request.json
    data_floats = [float(i) for i in body['data']]

    M, N, compareMode = body['M'], body['N'], body['compareMode']

    rec_plot = rp(M, N, data_floats, compareMode)
    image = rec_plot.draw_diagram()

    return send_file(image, attachment_filename=image, mimetype='image/png')


app.run(port=5000)
