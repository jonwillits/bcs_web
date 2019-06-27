from flask import Flask, render_template
import os
import pprint

from src.utils import load_content_and_submodules

app = Flask(__name__)

if os.getenv('APP_MODE') == "PRODUCTION":
    print('Loading production configs')
    app.config.from_object('production_configs')
else:
    print('Loading dev configs')
    app.config.from_object('dev_configs')

print('ENV', app.config['ENV'])
print('APPLICATION_ROOT', app.config['APPLICATION_ROOT'])

print('Current wd:', os.getcwd())


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/modules')
def modules():
    return render_template('modules.html')


@app.route('/module/<b>')
def module(b):
    static_path_name = app.config['STATIC_PATH_NAME']
    branch_path_name = b.replace('+', '/')
    content, submodules = load_content_and_submodules(static_path_name, branch_path_name)
    return render_template('module.html',
                           branch_nodes=b.replace('_', ' ').split('+'),
                           content=content,
                           submodules=submodules)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
