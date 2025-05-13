import unittest
from htmlnode import *

class HTMLNode_test(unittest.TestCase):
    def test_props_html(self): # Test prop to html conversion
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        expected = " href: https://www.google.com target: _blank"
        result = self.assertEqual(node.props_to_html(), expected)
        print(f"Test HTML: normal prop input")
#        print(f"Input: {node}")
#        print(f"Expected Result: {expected}")
#        print(f"Actual Result: {node.props_to_html()}")
#        print("")

    def test_props_none_type(self): # Test NoneType is passed through properly
        node = HTMLNode(props=None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
        print(f"Test HTML: prop value is None")

    
    def test_props_invalid_prop_type(self): # Test Type Error raised on non dict data (bit not NonType)
        node = HTMLNode(props=" href: https://www.google.com target: _blank")
        expected = "Incorrect prop type. Please ensure type is a Dictionary"
        with self.assertRaises(TypeError):
            node.props_to_html()
        print(f"Test HTML: prop value is Incorrect Data type")

if __name__ == "__main__":
    unittest.main()