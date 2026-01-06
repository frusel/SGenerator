import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_empty(self):
        node = HTMLNode(props = {})
        self.assertEqual(node.props_to_html(), "")

    def test_multiple(self):
        node = HTMLNode(props = {"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')



if __name__ == "__main__":
    unittest.main()