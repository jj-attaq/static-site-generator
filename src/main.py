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
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text1 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text1))
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

# [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

    # node = TextNode("This is a text node", "link", "https://www.boot.dev")
    # print(text_node_to_html_node(node))
    #
    # # node2 = TextNode("This is a node with **bold** text.", text_type_text)
    # # print(split_nodes_delimiter([node2], "**", text_type_bold))
    #
    # node3 = TextNode("This is a `code block` example", text_type_text)
    # print(split_nodes_delimiter([node3], "`", text_type_code))


    # print("========================================")
    # node2 = LeafNode(tag='a', value='Click me!', props={'href': 'https://example.com', 'target': '_blank'})
    # print(node2.props_to_html())
    # print(node2.__repr__())
    # print(node2.to_html())
    # node3 = LeafNode("p", "This is a paragraph of text.")
    # print(node3.to_html())  # should print: <p>This is a paragraph of text.</p>
    #
    # node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(node4.to_html())  # should print: <a href="https://www.google.com">Click me!</a>
    #
    # # Testing a node without a tag
    # node6 = LeafNode(None, "Just some text")
    # print(node6.to_html())  # should print: Just some text


main()
