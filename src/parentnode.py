from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid Parent: no tag")
        if self.children is None:
            raise ValueError("invalid Parent: no children")
        if len(self.children) == 0:
            raise ValueError("invalid Parent: children list is empty")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f"<{self.tag}>{children_string}</{self.tag}>"


        
        
