from flask import Flask, render_template
import os

from src.utils import load_content_and_submodules
from src import config

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


@app.route('/module/<branch>/')
@app.route('/module/<branch>/<leaf>')
def module(branch, leaf=config.Defaults.leaf):
    print('branch:', branch)
    print('leaf:', leaf)
    #
    branch_path_name = branch.replace('+', '/')
    md_file_name = '{}.md'.format(leaf)
    static_path_name = app.config['STATIC_PATH_NAME']
    content, submodules = load_content_and_submodules(static_path_name,
                                                      branch_path_name,
                                                      md_file_name)
    return render_template('module.html',
                           nodes=branch.replace('_', ' ').split('+'),
                           heading=leaf.replace('_', ' ').capitalize(),
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
