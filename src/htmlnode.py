class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("Value is required")
        super().__init__(tag, value, None, props)
    
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