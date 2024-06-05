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
