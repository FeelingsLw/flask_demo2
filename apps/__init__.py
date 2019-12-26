from flask import Flask
from apps.goods import goods
from apps import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/hello')
def hello():
    return "Hello Flask!!!!!12312312"


app.register_blueprint(goods)
