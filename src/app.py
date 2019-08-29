from flask import Flask, render_template, url_for, request, session, redirect
import os
from pathlib import Path

from src.utils import load_content
from src.utils import get_leaves_for_pagination
from src.utils import get_password
from src.utils import to_area
from src.utils import sort_numerically
from src import config

app = Flask(__name__)

if os.getenv('APP_MODE') == "PRODUCTION":
    print('Loading production configs')
    app.config.from_object('production_configs')
else:
    print('Loading dev configs')
    app.config.from_object('dev_configs')


@app.route('/x')  # TODO remove
def x():
    session.clear()
    return redirect(url_for('modules'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/modules')
def modules():
    return render_template('modules.html')


@app.route('/module/<path:branch>/')
@app.route('/module/<path:branch>/leaf=<string:leaf>')
def module(branch, leaf=config.Defaults.leaf):

    print('======================= {} {} requested'.format(branch, leaf))

    # init session
    if 'allowed_area_names' not in session:
        session['allowed_area_names'] = []

    # check access rights
    area = to_area(branch, leaf)
    restricted_areas = [val for val in os.environ if val.startswith(branch)]
    allowed_area_names = session['allowed_area_names']
    if area in restricted_areas and area not in allowed_area_names:
        return render_template('login.html',
                               branch=branch,
                               leaf=leaf,
                               heading=area.replace('_', ' '))

    # content_path
    static_path_name = app.config['STATIC_PATH_NAME']
    content_path = Path(static_path_name) / branch.lower()

    # load content
    md_file_name = '{}.md'.format(leaf)
    main_content, side_content = load_content(content_path, md_file_name)

    # pagination
    md_file_names = sort_numerically([p.stem for p in content_path.glob('*.md')])
    print(content_path)
    print(md_file_names)
    default_leaf, next_leaf, previous_leaf = get_leaves_for_pagination(leaf, md_file_names)
    print(previous_leaf)
    print(next_leaf)

    return render_template('module.html',
                           nodes=branch.split('/'),
                           main_content=main_content,
                           side_content=side_content,
                           restricted_area_nums=[str(int(area.split('_')[-1])) for area in restricted_areas],
                           allowed_area_nums=[str(int(area.split('_')[-1])) for area in allowed_area_names],
                           default_leaf=default_leaf,
                           previous_leaf=previous_leaf,
                           next_leaf=next_leaf)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login/<path:branch>/leaf=<string:leaf>', methods=['POST'])
def do_login(branch, leaf=config.Defaults.leaf):
    area_name = to_area(branch, leaf)
    if request.form['password'] == get_password(area_name):
        session['allowed_area_names'] += [area_name]  # appending does not work (not clear why)
    else:
        if not session.get('num_attempts'):
            session['num_attempts'] = 1
        else:
            session['num_attempts'] += 1

    return redirect(url_for('module', branch=branch, leaf=leaf))


if __name__ == '__main__':
    app.run(debug=True if os.getenv('APP_MODE') != 'PRODUCTION' else False)
