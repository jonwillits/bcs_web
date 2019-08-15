from flask import Flask, render_template, flash, request, session
import os
from pathlib import Path

from src.utils import load_content, get_leaves_for_pagination
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

    # TODO password protect some urls

    if '10_' in leaf and not session.get('logged_in'):
        return render_template('login.html')

    # content_path
    static_path_name = app.config['STATIC_PATH_NAME']
    content_path = Path(static_path_name) / branch.lower()

    # load content
    md_file_name = '{}.md'.format(leaf)
    main_content, side_content = load_content(content_path, md_file_name)

    # pagination
    md_file_names = sorted([p.stem for p in content_path.glob('*.md')])
    default_leaf, next_leaf, previous_leaf = get_leaves_for_pagination(leaf, md_file_names)

    return render_template('module.html',
                           nodes=branch.split('/'),
                           heading=to_heading(branch, leaf),
                           main_content=main_content,
                           side_content=side_content,
                           default_leaf=default_leaf,
                           previous_leaf=previous_leaf,
                           next_leaf=next_leaf)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()



if __name__ == '__main__':
    app.run(debug=True)
