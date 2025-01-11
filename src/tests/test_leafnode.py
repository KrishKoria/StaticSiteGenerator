import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leafnode_initialization(self):
        node = LeafNode(tag='p', value='This is a paragraph.', props={'class': 'text'})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'This is a paragraph.')
        self.assertEqual(node.props, {'class': 'text'})
    
    def test_leafnode_to_html(self):
        node = LeafNode(tag='p', value='This is a paragraph.', props={'class': 'text'})
        self.assertEqual(node.to_html(), '<p class="text">This is a paragraph.</p>')
    
    def test_leafnode_to_html_no_props(self):
        node = LeafNode(tag='p', value='This is a paragraph.', props={})
        self.assertEqual(node.to_html(), '<p>This is a paragraph.</p>')
    
    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(tag=None, value='This is just text.', props={})
        self.assertEqual(node.to_html(), 'This is just text.')


if __name__ == '__main__':
    unittest.main()