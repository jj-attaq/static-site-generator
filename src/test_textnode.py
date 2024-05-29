import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", "bold", "www.example.com")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", "bold", "www.example.com")
        node6 = TextNode(None, "bold", "www.example.com")
        self.assertNotEqual(node5, node6)

        node7 = TextNode("This is a text node", "bold", "www.example.com")
        node8 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node7, node8)

    # def test_repr(self):
    #     node = TextNode("This is a text node", "bold", "www.example.com")
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "www.example.com")
        self.assertEqual(
            "TextNode(This is a text node, bold, www.example.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
