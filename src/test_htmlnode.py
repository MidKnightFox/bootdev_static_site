import unittest
from htmlnode import *

class HTMLNode_test(unittest.TestCase):
    def test_props_html(self): # Test prop to html conversion
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        expected = " href: https://www.google.com target: _blank"
        result = self.assertEqual(node.props_to_html(), expected)
        print(f"Test normal prop input")
        print(f"Input: {node}")
        print(f"Expected Result: {expected}")
        print(f"Actual Result: {node.props_to_html()}")
        print("")

    def test_props_none_type(self):
        node = HTMLNode(props=None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
        print(f"Test prop value is None")
        print(f"Input: {node}")
        print(f"Expected Result: {expected}")
        print(f"Actual Result: {node.props_to_html()}")
        print("")
    
    def test_props_invalid_prop_type(self):
        node = HTMLNode(props=" href: https://www.google.com target: _blank")
        expected = "Incorrect prop type. Please ensure type is a Dictionary"
        self.assertRaises(node.props_to_html(), expected)
        print(f"Test prop value is None")
        print(f"Input: {node}")
        print(f"Expected Result: {expected}")
        print(f"Actual Result: {node.props_to_html()}")
        print("")

if __name__ == "__main__":
    unittest.main()