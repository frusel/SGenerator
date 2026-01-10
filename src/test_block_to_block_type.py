import unittest

from block_markdown import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_heading_basic(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### H6"), BlockType.HEADING)

    def test_heading_not_heading(self):
        self.assertEqual(block_to_block_type("#Heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

    def test_codeblock_basic(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_codeblock_with_language(self):
        block = "```python\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_codeblock_not_closed(self):
        block = "```\nprint('hi')\n"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_block_basic(self):
        block = "> a\n> b\n> c"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_allows_empty_content(self):
        block = "> \n> test"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_mixed_lines_not_allowed(self):
        block = "> a\nb"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_basic(self):
        block = "- a\n- b\n- c"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_allows_empty_items(self):
        block = "- \n- test"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_mixed_lines_not_allowed(self):
        block = "- a\nb"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_basic(self):
        block = "1. a\n2. b\n3. c"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_allows_empty_items(self):
        block = "1. \n2. test"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_at_1(self):
        block = "2. a\n3. b"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_must_increment_by_1(self):
        block = "1. a\n3. b"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Line 1\nLine 2"), BlockType.PARAGRAPH)

    def test_windows_newlines_are_handled(self):
        block = "1. a\r\n2. b\r\n3. c"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()