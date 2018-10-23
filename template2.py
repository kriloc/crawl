from flask import render_template
from flask import Flask

import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    return None


if __name__ == '__main__':
    app.run()