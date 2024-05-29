class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Next, create an __eq__ method that returns True if all of the properties
    # of two TextNode objects are equal.
    def __eq__(self, other_node):
        return (
            self.text == other_node.text and
            self.text_type == other_node.text_type and
            self.url == other_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
