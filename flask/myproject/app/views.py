__author__ = 'xuxiongjian'
import app

@app.route('/')
def index():
    return '12323224242334'

@app.route('project')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

