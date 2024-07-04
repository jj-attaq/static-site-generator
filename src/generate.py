import os
# import shutil

from markdown_blocks import markdown_to_html_node


def extract_title(md):
    lines = md.split('\n')
    title = None
    for line in lines:
        if line.startswith('# '):
            title = line
            return title
            break
    if title is None:
        raise Exception('All pages need a single h1 header')


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    # save markdown from_path to variable
    md = open(from_path).read()
    template = open(template_path).read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)

    dir = os.path.dirname(dest_path)
    os.makedirs(dir)

    file = open(dest_path, 'w')
    file.write(template)
#
#
#
# generate_page('./content/index.md', './template.html', 'hoho/lala/haha.html')
