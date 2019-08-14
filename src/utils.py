import markdown
from pathlib import Path

from src import config


def to_heading(branch, leaf):
    if leaf == config.Defaults.leaf:
        return branch.split('/')[-1].replace('_', ' ')
    else:
        return ' '.join([w.capitalize() for w in leaf.split('_')])


def open_file(content_path, file_name):
    p = content_path / file_name
    if not p.exists():
        f = None
    else:
        f = p.open('r')
    return f


def default_content(md_file_name):
    if md_file_name == config.Defaults.leaf + '.md':
        return "<h2>Content coming soon...</h2>" \
               "<h3><a href='/modules' style='text-decoration: none;'>&lArr; Return to Modules</a></h3>"
    else:
        return "<h2>Content coming soon...</h2>"


def load_content_and_submodules(static_path_name, branch_path_name, md_file_name):

    content_path = Path(static_path_name) / branch_path_name.lower()

    # submodules
    sm_file_name = 'submodules.html'
    sm_file = open_file(content_path, sm_file_name)
    if sm_file is None:
        print('Did not find {} in:\n{}'.format(sm_file_name, content_path))
        return default_content(md_file_name), None
    submodules = sm_file.read()

    # content
    md_file = open_file(content_path, md_file_name)
    if md_file is None:
        print('Did not find {} in:\n{}'.format(md_file_name, content_path))
        return default_content(md_file_name), submodules
    md = md_file.read()
    content = markdown.markdown(md, extensions=['extra', 'smarty'], output_format='html5')

    return content, submodules
