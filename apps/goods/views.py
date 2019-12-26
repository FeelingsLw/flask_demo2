from apps.goods import goods
from flask import render_template

@goods.route('/index')
def index():

    return render_template('index.html', m={'msg': '我是消息'})
