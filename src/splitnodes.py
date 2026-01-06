from textnode import TextType, TextNode

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

