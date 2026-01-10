from textnode import TextType, TextNode
from extract_markdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_text = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or delimiter not in old_node.text:
            split_text.append(old_node)
        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise Exception("invalid Markdown: unmatched delimiters")
            old_node_split_text = old_node.text.split(delimiter)
            node_type = TextType.TEXT
            for new_node in old_node_split_text:
                if new_node != "":
                    split_text.extend([TextNode(new_node, node_type)])
                if node_type == TextType.TEXT:
                    node_type = text_type
                else:
                    node_type = TextType.TEXT
            
    return split_text

def split_nodes_link(old_nodes):
    split_nodes = []
    for old_node in old_nodes:
        markdown_links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text
        if old_node.text_type != TextType.TEXT or markdown_links == []:
            split_nodes.append(old_node)
        else:
            for markdown_text, markdown_url in markdown_links:
                before, after = remaining_text.split(f"[{markdown_text}]({markdown_url})", 1)
                remaining_text = after
                if before != "":
                    split_nodes.append(TextNode(before, TextType.TEXT))
                split_nodes.append(TextNode(markdown_text, TextType.LINK, markdown_url))
            if remaining_text != "":
                split_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return split_nodes

def split_nodes_image(old_nodes):
    split_nodes = []
    for old_node in old_nodes:
        markdown_links = extract_markdown_images(old_node.text)
        remaining_text = old_node.text
        if old_node.text_type != TextType.TEXT or markdown_links == []:
            split_nodes.append(old_node)
        else:
            for markdown_text, markdown_url in markdown_links:
                before, after = remaining_text.split(f"![{markdown_text}]({markdown_url})", 1)
                remaining_text = after
                if before != "":
                    split_nodes.append(TextNode(before, TextType.TEXT))
                split_nodes.append(TextNode(markdown_text, TextType.IMAGE, markdown_url))
            if remaining_text != "":
                split_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return split_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    link = split_nodes_link(code)
    final = split_nodes_image(link)
    return final
    






