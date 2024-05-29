from textnode import TextNode
from htmlnode import HTMLNode, LeafNode


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__repr__())
    print("========================================")
    node2 = HTMLNode(tag='a', value='Click me!', props={'href': 'https://example.com', 'target': '_blank'})
    print(node2.props_to_html())
    print(node2.__repr__())
    print(node2.to_html())
    node3 = LeafNode("p", "This is a paragraph of text.")
    print(node3.to_html())  # should print: <p>This is a paragraph of text.</p>

    node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node4.to_html())  # should print: <a href="https://www.google.com">Click me!</a>

    # Testing a node without a tag
    node6 = LeafNode(None, "Just some text")
    print(node6.to_html())  # should print: Just some text


main()
