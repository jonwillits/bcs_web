import yaml
import markdown
from pathlib import Path


DEFAULT_CONTENT = '''
<h2>Content coming soon...</h2>
<h3><a href='/modules' style="text-decoration: none;">&lArr; Back to Modules</a></h3>

'''

DEFAULT_META = {'submodules': (('Overview', ['Coming Soon...']), ('Overview', ['Coming Soon...'])),
                'misc': (('Homework', ['Coming Soon...']), ('Homework', ['Coming Soon...']))}


def open_file(content_path, file_name):
    p = content_path / file_name
    if not p.exists():
        f = None
    else:
        f = p.open('r')
    return f


def load_content_and_meta(static_path_name, branch_path_name):

    content_path = Path(static_path_name) / branch_path_name.lower()

    # content
    md_file_name = 'intro.md'
    md_file = open_file(content_path, md_file_name)
    if md_file is None:
        print('Did not find {} in:\n{}'.format(md_file_name, content_path))
        return DEFAULT_CONTENT, DEFAULT_META
    md = md_file.read()
    content = markdown.markdown(md, extensions=['extra', 'smarty'], output_format='html5')

    # meta
    yaml_file_name = 'meta.yaml'
    yaml_file = open_file(content_path, yaml_file_name)
    if yaml_file is None:
        print('Did not find {} in:\n{}'.format(yaml_file_name, content_path))
        return DEFAULT_CONTENT, DEFAULT_META
    meta = yaml.load(yaml_file)

    return content, meta
