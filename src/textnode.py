from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return (
            self.text == other_node.text and
            self.text_type == other_node.text_type and
            self.url == other_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    def get_valid_url():
        url = text_node.url
        if url is None:
            raise Exception("text_node requires text_node.url field")
        else:
            return url

    if text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text).to_html()

    elif text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value=text_node.text).to_html()

    elif text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value=text_node.text).to_html()

    elif text_node.text_type == text_type_code:
        return LeafNode(tag="code", value=text_node.text).to_html()

    elif text_node.text_type == text_type_link:
        return LeafNode(tag="a", value=text_node.text, props={"href": get_valid_url()}).to_html()

    elif text_node.text_type == text_type_image:
        return LeafNode(tag="img", value="", props={"src": get_valid_url(), "alt": text_node.text}).to_html()

    else:
        raise Exception("text_node needs valid type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            split_node = node.text.split(delimiter)
            inside_delimiter = False

            for s_node in split_node:
                print(f'Splitting: "{s_node}" inside_delimiter: {inside_delimiter}')
                if inside_delimiter:
                    result.append(TextNode(s_node, text_type))
                else:
                    result.append(TextNode(s_node, "text"))
                # print(inside_delimiter)
                inside_delimiter = not inside_delimiter
            if len(split_node) % 2 == 0:
                raise ValueError("Mismatched delimiter")

        else:
            result.append(node)

    return result
