import os
# import shutil

from markdown_blocks import markdown_to_html_node


def extract_title(md):
    lines = md.split('\n')
    title = None
    for line in lines:
        if line.startswith('# '):
            title = line[2:]
            return title
    if title is None:
        raise Exception('All pages need a single h1 header')


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    # save markdown from_path to variable
    from_file = open(from_path)
    md = from_file.read()
    from_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path) and from_path[-3:] == '.md':
            dest_path = dest_path[:-3] + '.html'
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
