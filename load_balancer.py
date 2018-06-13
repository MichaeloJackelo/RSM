from flask import Flask
import flask_profiler
import http.client
from itertools import cycle


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite",
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    }
}


flask_profiler.init_app(app)


class RoundRobin():
    next_elem = {}
    li = [5001, 5002, 5003]
    licycle = cycle(li)

    def get_next_port(self):
        self.next_elem = next(i.licycle)
        return self.next_elem


i = RoundRobin()


@app.route('/calculate_pi/<id>')
@flask_profiler.profile()
def balance_request(id):
    conn = http.client.HTTPConnection("www.localhost:" + str(i.get_next_port()))
    conn.request("GET", "/calculate_pi/3")
    r1 = conn.getresponse()
    data = r1.read()
    return data
