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
    split_nodes_image
    )


def main():
    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and a third ![third image](https://search.brave.com/images?q=image)",
        text_type_text,
    )
    new_nodes = split_nodes_image([node])
    # print(new_nodes)


main()
