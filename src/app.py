from flask import Flask, render_template
import os
from pathlib import Path

from src.utils import load_content_and_submodules, get_leaves_for_pagination
from src.utils import to_heading
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


@app.route('/module/<path:branch>/')
@app.route('/module/<path:branch>/leaf=<leaf>')
def module(branch, leaf=config.Defaults.leaf):
    print('branch:', branch)
    print('leaf:', leaf)

    # content, submodules
    static_path_name = app.config['STATIC_PATH_NAME']
    branch_path_name = branch
    md_file_name = '{}.md'.format(leaf)
    content, submodules = load_content_and_submodules(static_path_name,
                                                      branch_path_name,
                                                      md_file_name)
    # pagination
    module_path = Path('static') / 'content' / branch.lower()
    md_file_names = sorted([p.stem for p in module_path.glob('*.md')])
    default_leaf, next_leaf, previous_leaf = get_leaves_for_pagination(leaf, md_file_names)

    return render_template('module.html',
                           nodes=branch.split('/'),
                           heading=to_heading(branch, leaf),
                           content=content,
                           submodules=submodules,
                           default_leaf=default_leaf,
                           previous_leaf=previous_leaf,
                           next_leaf=next_leaf)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
