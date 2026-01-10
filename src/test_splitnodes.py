import unittest

from textnode import TextType, TextNode
from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textnodes


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

    def test_split_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        ) 

    def test_split_one_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
                
            ],
            new_nodes,
        ) 

    def test_split_one_image_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
                
            ],
            new_nodes,
        ) 

    def test_split_one_image_end(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                
            ],
            new_nodes,
        ) 

    def test_split_no_image(self):
        node = TextNode(
            "This is text with an and another",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an and another", TextType.TEXT),
                
                
            ],
            new_nodes,
        ) 

    def test_split_image_other_texttype(self):
        
        node = TextNode(
            "This is a Linktext",
            TextType.LINK,
            "google.de"
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a Linktext", TextType.LINK, "google.de"),
                
                
            ],
            new_nodes,
        ) 

    def test_text_to_testnotes(self):
        
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            
        
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        ) 
    


   
    

if __name__ == "__main__":
    unittest.main()