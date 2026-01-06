import unittest

from textnode import TextType, TextNode
from splitnodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("just plain text", TextType.TEXT)
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("just plain text", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_single_segment(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This is " , TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" text", TextType.TEXT)         
                    ]
        self.assertEqual(actual, expected)

    def test_double_segment(self):
        node = TextNode("This is **bold** and **bolder** text", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This is " , TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("bolder", TextType.BOLD),  
                    TextNode(" text", TextType.TEXT),      
                    ]
        self.assertEqual(actual, expected)

    def test_start_end(self):
        node = TextNode("**Bold Text**", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
                    TextNode("Bold Text", TextType.BOLD),    
                    ]
        self.assertEqual(actual, expected)

    def test_odd_number_of_delimiters_raises(self):
        node = TextNode("This is **broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)


   
    

if __name__ == "__main__":
    unittest.main()