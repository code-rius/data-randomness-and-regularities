import flask, os
import numpy as np

from flask import request, send_file
from recurrence_plot import RecurrencePlot as rp

app = flask.Flask(__name__)
app.config['DEBUG'] = True

path = os.path.dirname(os.path.realpath(__file__))


@app.route('/', methods=['GET', 'POST'])
def index():
    return {'Reponse': 'success'}


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
