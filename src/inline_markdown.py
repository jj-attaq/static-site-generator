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
        if old_node.text_type != text_type_text:
            result.append(old_node)
            continue
        text = old_node.text
        image_tup = extract_markdown_images(text)
        if not image_tup:
            result.append(TextNode(text, text_type_text))
            continue  # Skip to the next old_node if no images found

        for image in image_tup:
            split = text.split(f"![{image[0]}]({image[1]})", 1)
            text = split[1]
            if split[0]:
                result.append(TextNode(split[0], text_type_text))
            result.append(TextNode(image[0], text_type_image, image[1]))
        if text:
            result.append(TextNode(text, text_type_text))
    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
            continue
        text = old_node.text
        link_tup = extract_markdown_links(text)
        if not link_tup:
            result.append(TextNode(text, text_type_text))
            continue  # Skip to the next old_node if no links found

        for link in link_tup:
            split = text.split(f"[{link[0]}]({link[1]})", 1)
            text = split[1]
            if split[0]:
                result.append(TextNode(split[0], text_type_text))
            result.append(TextNode(link[0], text_type_link, link[1]))
        if text:
            result.append(TextNode(text, text_type_text))
    return result

# ORIGINAL BELOW
# def split_nodes_image(old_nodes):
#     result = []
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             result.append(old_node)
#             continue
#         text = old_node.text
#         image_tup = extract_markdown_images(text)
#         if image_tup == []:
#             result.append(TextNode(text, text_type_text))
#         for i in range(len(image_tup)):
#             split = text.split(f"![{image_tup[i][0]}]({image_tup[i][1]})", 1)
#             text = split[1]
#             if split[0] != "":
#                 result.append(TextNode(split[0], text_type_text))
#             result.append(TextNode(image_tup[i][0], text_type_image, image_tup[i][1]))
#             if i == len(image_tup) - 1 and split[1] != "":
#                 result.append(TextNode(split[1], text_type_text))
#         #
#         # for i in range(len(result)):
#         #     print(result[i], end="\n")
#     return result
#
#
# def split_nodes_link(old_nodes):
#     result = []
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             result.append(old_node)
#             continue
#         text = old_node.text
#         link_tup = extract_markdown_links(text)
#         if not link_tup:
#             result.append(TextNode(text, text_type_text))
#             continue
#         for i in range(len(link_tup)):
#             split = text.split(f"[{link_tup[i][0]}]({link_tup[i][1]})", 1)
#             text = split[1]
#             if split[0] != "":
#                 result.append(TextNode(split[0], text_type_text))
#             result.append(TextNode(link_tup[i][0], text_type_link, link_tup[i][1]))
#             if i == len(link_tup) - 1 and split[1] != "":
#                 result.append(TextNode(split[1], text_type_text))
#         #
#         # for i in range(len(result)):
#         #     print(result[i], end="\n")
#     return result

