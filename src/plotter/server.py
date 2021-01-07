import flask, os
import numpy as np
import tensorflow as tf

from flask import request, send_file, make_response, jsonify
from recurrence_plot import RecurrencePlot as rp

from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from PIL import Image

app = flask.Flask(__name__)
app.config['DEBUG'] = True
image_filename = 'recurrence_plot_image.png'

path = os.path.dirname(os.path.realpath(__file__))
def enable_gpu():
    # Optional - enable GPU accelleration
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    print("Num GPUs Available: ", len(physical_devices))
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

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


enable_gpu()
get_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('Hello world!')



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

    M, N, compareMode, target = body['M'], body['N'], body['compareMode'], body['pixelTarget']

    print(target)
    rec_plot = rp(M, N, data_floats, compareMode, target)
    rec_plot.draw_diagram(image_filename)
    response = make_response(
        send_file(image_filename, attachment_filename=image_filename, mimetype='image/png'))

    im = Image.open(image_filename)

    processed_image = preprocess_image(im, target_size=(224, 224))
    prediction = model.predict(processed_image).tolist()
    print(prediction)
    
    response.headers['X-periodic'] = np.round(prediction[0][0], 5)
    response.headers['X-trend'] = np.round(prediction[0][1], 5)
    response.headers['X-chaotic'] = np.round(prediction[0][2], 5)

    return response


app.run(port=5000)
