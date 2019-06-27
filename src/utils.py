import markdown
from pathlib import Path


DEFAULT_CONTENT = '''
<h2>Content coming soon...</h2>
<h3><a href='/modules' style="text-decoration: none;">&lArr; Back to Modules</a></h3>

'''

DEFAULT_META = """
<li>
<a href="#" class="dropdown-jw">Default<span class="caret"></span></a>
<ul class="collapse list-unstyled" class="dropdown-jw-container">
    <a href="#">d1</a>
    <a href="#">d2</a>
    <a href="#">d3</a>
</ul>
</li>
"""


def open_file(content_path, file_name):
    p = content_path / file_name
    if not p.exists():
        f = None
    else:
        f = p.open('r')
    return f


def load_content_and_submodules(static_path_name, branch_path_name, md_file_name):

    content_path = Path(static_path_name) / branch_path_name.lower()

    # content
    md_file = open_file(content_path, md_file_name)
    if md_file is None:
        print('Did not find {} in:\n{}'.format(md_file_name, content_path))
        return DEFAULT_CONTENT, DEFAULT_META
    md = md_file.read()
    content = markdown.markdown(md, extensions=['extra', 'smarty'], output_format='html5')

    sm_file_name = 'submodules.html'
    sm_file = open_file(content_path, sm_file_name)
    if sm_file is None:
        print('Did not find {} in:\n{}'.format(sm_file_name, content_path))
        return DEFAULT_CONTENT, DEFAULT_META
    submodules = sm_file.read()

    return content, submodules
