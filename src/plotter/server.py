import flask, os, uuid
import numpy as np

from flask import request
from recurrence_plot import RecurrencePlot as rp
from tinydb import TinyDB, Query


app = flask.Flask(__name__)
app.config['DEBUG'] = True


path = os.path.dirname(os.path.realpath(__file__))
db = TinyDB(path + '/assets/plot-data.json')


class get_current_user():
    username = 'Audrius'
    theme = 'Dark'


@app.route('/', methods=['GET', 'POST'])
def index():
    print(uuid.uuid4())
    return {'Reponse': 'success'}


@app.route('/recurrence_plot/<data>', methods=['POST'])
def me_api(data):
    user = get_current_user()
    print('=======Request data coming in=======')
    print(request.form)
    print('=======end of request data =======')
    uploaded_file = request.files['csvdata']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        print(uploaded_file.filename)
    return {
        'data': data,
        'theme': user.theme,
        'username': user.username
    }


@app.route('/get_plot_data', methods=['GET'])
def get_plot_data():
    path = os.path.dirname(os.path.realpath(__file__))
    print(os.listdir(path + '/assets/'))
    return {'Hello': 'Hellooo'}


@app.route('/plot_json/', methods=['POST'])
def plot_json():
    data_strings = request.json['data']
    params = request.json['params']
    data_floats = [float(i) for i in data_strings]

    M, N, compareMode = params['M'], params['N'], params['compareMode']

    rec_plot = rp(M, N, data_floats, compareMode)
    # rec_plot.draw_diagram()

    return {
        'plot_data': rec_plot.similarities
    }


app.run(port=5000)
