import unittest
from htmlnode import *

class HTMLNODE(unittest.TestCase):
    def test_props_html(self): # Test prop to html conversion
        node = HTMLNODE(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(HTMLNODE.props(), "href: https://www.google.com","target: _blank")

if __name__ == "__main__":
    unittest.main()