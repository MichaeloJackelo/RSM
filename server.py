from decimal import Decimal, getcontext
from flask import Flask
import flask_profiler


def calculate_pi_Bailey_Borwein_Plouffe_formula(start, end):
    getcontext().prec=6000
    return str(sum(1/Decimal(16)**k *
                (Decimal(4)/(8*k+1) -
                 Decimal(2)/(8*k+4) -
                 Decimal(1)/(8*k+5) -
                 Decimal(1)/(8*k+6)) for k in range(start, end)))


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    }
}


flask_profiler.init_app(app)


@app.route('/calculate_pi/<id>')
@flask_profiler.profile()
def calculate_pi(id):
    return calculate_pi_Bailey_Borwein_Plouffe_formula(0, 1000) + ' id = ' + str(id)