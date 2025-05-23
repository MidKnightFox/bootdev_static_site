import unittest
from htmlnode import *

## Unit tests for HTMLNode class
class HTMLNode_test(unittest.TestCase):
    def test_props_html(self): # Test prop to html conversion
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        expected = " href: https://www.google.com target: _blank"
        result = self.assertEqual(node.props_to_html(), expected)
        #print(f"Test HTML: normal prop input")
#        print(f"Input: {node}")
#        print(f"Expected Result: {expected}")
#        print(f"Actual Result: {node.props_to_html()}")
#        print("")

    def test_props_none_type(self): # Test NoneType is passed through properly
        node = HTMLNode(props=None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
        #print(f"Test HTML: prop value is None")

    
    def test_props_invalid_prop_type(self): # Test Type Error raised on non dict data (bit not NonType)
        node = HTMLNode(props=" href: https://www.google.com target: _blank")
        expected = "Incorrect prop type. Please ensure type is a Dictionary"
        with self.assertRaises(TypeError):
            node.props_to_html()
        #print(f"Test HTML: prop value is Incorrect Data type")

#class LeafNode_test(unittest.TestCase):
## Tests for LeafNode
    def test_leaf_to_html_p(self): # Test basic text an tag is converted correctly
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        #print(f"Test LeafNode: Leaf to Basic HTML")

    def test_leaf_to_html_p_href(self): # Test text and tag with a prop is converted correcly
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        #print(f"Test LeafNode: Leaf to HTML with href/ link")
    
    #Add tests for when the VALUE arguements are not entered. These should fail and raise a value error
    #Add tests for when no TAG arguement is entered. This should just return the VALUE input as text. No modification

#class ParentNode(unittest.TestCase):
## Tests for ParentNode
    #Site Provided tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    #Provided from answers
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    #End provided from answers

# This line allows the tests to be run automatically. Leave at end of the file
if __name__ == "__main__": # a conditional that checks if the script is being run directly or imported as a module
    unittest.main() # discovers the unit tests that need to be run

