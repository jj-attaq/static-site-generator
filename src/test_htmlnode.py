import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag='a', value='Click me!', props={'href': 'https://example.com', 'target': '_blank'})
        node2 = HTMLNode(tag='a', value='Click me!', props={'href': 'https://example.com', 'target': '_blank'})
        self.assertEqual(node, node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()

    # def test_repr(self):
    #     node = TextNode("This is a text node", "bold", "www.example.com")
    #     self.assertEqual(
    #         "TextNode(This is a text node, bold, www.example.com)", repr(node)
    #     )
