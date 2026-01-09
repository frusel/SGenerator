import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_one_image(self):
        actual = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)")
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(actual, expected)

    def test_mult_image(self):
        actual = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(actual, expected)

    def test_no_image(self):
        actual = extract_markdown_images("This is just a text")
        expected = []
        self.assertEqual(actual, expected)

    def test_mult_link(self):
        actual = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual, expected)

    def test_no_link(self):
        actual = extract_markdown_links("This is just a text")
        expected = []
        self.assertEqual(actual, expected)

    def test_one_link(self):
        actual = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()