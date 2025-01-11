from src.htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        if props_html:
            return f'<{self.tag} {props_html}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'