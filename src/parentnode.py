from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props or None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Children are required")
    
        props_html = self.props_to_html() if self.props else ""
        children_html = ' '.join([child.to_html() for child in self.children])
        return f"<{self.tag} {props_html}>{children_html}</{self.tag}>"