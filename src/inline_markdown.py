import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
            continue

        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("Mismatched delimiter")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(split_node[i], text_type_text))
            else:
                result.append(TextNode(split_node[i], text_type))

    return result


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        text = old_node.text
        new_nodes = []
        image_tup = extract_markdown_images(text)
        for img in image_tup:
            split = text.split(f"![{img[0]}]({img[1]})", 1)
            text = split[1]
            new_nodes.append(TextNode(split[0], text_type_text))
            new_nodes.append(TextNode(img[0], text_type_image, img[1]))
        result.append(new_nodes)

        for i in range(len(new_nodes)):
            print(new_nodes[i], end="\n")
    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        text = old_node.text
        new_nodes = []
        link_tup = extract_markdown_images(text)
        for link in link_tup:
            split = text.split(f"[{link[0]}]({link[1]})", 1)
            text = split[1]
            new_nodes.append(TextNode(split[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_image, link[1]))
        result.append(new_nodes)

        for i in range(len(new_nodes)):
            print(new_nodes[i], end="\n")
    return result
