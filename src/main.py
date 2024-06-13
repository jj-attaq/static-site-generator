from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    TextNode,
    text_node_to_html_node,
)
from inline_markdown import (
    # split_nodes_delimiter,
    # extract_markdown_images,
    # extract_markdown_links,
    text_to_textnodes
    )


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)


main()
