import flask
import os
import uuid
import numpy as np

from flask import request
from recurrence_plot import RecurrencePlot as rp
from tinydb import TinyDB, Query


app = flask.Flask(__name__)
app.config['DEBUG'] = True


path = os.path.dirname(os.path.realpath(__file__))
db = TinyDB(path + '/assets/plot-data.json')

db.insert({
    "id": "adffb6ce-bbd2-46e3-ba59-940f2db7e5a2",
    "name": "Dow Jones Data",
    "params": {
        "Downsize": "false",
        "M": 3,
        "N": 2,
        "compareMode": 0
    }
})

print(db.all())
