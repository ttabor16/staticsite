import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eqURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://someurl.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://someurl.com")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_noteqURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://someurl.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://someurl.gov")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()