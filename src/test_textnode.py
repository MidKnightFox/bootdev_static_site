import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self): # Nodes are Equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self): # Nodes are not equal (type difference)
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_ne_2(self): # Nodes not equal (text difference)
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none(self): # URL is NONE when set to None manually or default
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url, node2.url)

if __name__ == "__main__":
    unittest.main()