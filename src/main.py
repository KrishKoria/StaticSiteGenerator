from textnode import TextNode
from .leafnode import LeafNode
from .textnode import TextType
def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode)

def text_node_to_html_node(text_node):
    if text_node.type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.href})
    elif text_node.type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.src, "alt": text_node.alt})
    else:
        raise ValueError("Unsupported TextNode type")

if __name__ == "__main__":
    main()