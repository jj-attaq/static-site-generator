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
    split_nodes_image,
    split_nodes_link
    )


def main():
    # Testing with no images and no links
    node = TextNode("This text has no images or links.", text_type_text)
    new_image_nodes = split_nodes_image([node])
    new_link_nodes = split_nodes_link([node])

    print(new_image_nodes)  # Expecting: [TextNode("This text has no images or links.", text_type_text)]
    print(new_link_nodes)   # Expecting: [TextNode("This text has no images or links.", text_type_text)]


main()
