import markdown
import os

from src import config


def get_password(branch, leaf):
    supplied_key = '{}_{}'.format(branch, leaf[1:3])  # e.g. extract "07" from a leaf named "m07_3_1"
    return os.getenv(supplied_key)


def is_leaf_restricted(branch, leaf):
    val = get_password(branch, leaf)

    print('val')
    print(val)

    if val is not None:
        return True
    else:
        return False


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


def load_content(content_path, md_file_name):

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


def get_leaves_for_pagination(leaf, md_file_names):
    try:
        file_name_idx = md_file_names.index(leaf)
    except ValueError:
        previous_leaf = None
        next_leaf = None
    else:
        if leaf == config.Defaults.leaf:  # don't show 'prev' button
            previous_leaf = None
            next_leaf = md_file_names[file_name_idx + 1]
        elif file_name_idx + 1 == len(md_file_names):  # don't show 'next' button
            previous_leaf = md_file_names[file_name_idx - 1]
            next_leaf = None
        else:
            previous_leaf = md_file_names[file_name_idx - 1]
            next_leaf = md_file_names[file_name_idx + 1]

    return config.Defaults.leaf, next_leaf, previous_leaf
