import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag='div', props={'class': 'container'})
        self.assertEqual(node.props_to_html(), 'class="container"')
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag='a', props={'href': 'https://example.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank"')
    
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag='span', props={})
        self.assertEqual(node.props_to_html(), '')

if __name__ == '__main__':
    unittest.main()