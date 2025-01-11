import unittest
from src.parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_parentnode_initialization(self):
        node = ParentNode(tag='div', children=[])
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.children, [])
        self.assertIsNone(node.props)

    def test_parentnode_to_html_no_tag(self):
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Tag is required")

    def test_parentnode_to_html_no_children(self):
        node = ParentNode(tag='div', children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Children are required")

    def test_parentnode_to_html_empty_children(self):
        node = ParentNode(tag='div', children=[])
        self.assertEqual(node.to_html(), "<div ></div>")

    def test_parentnode_no_children(self):
        node = ParentNode(tag='div', children=[])
        self.assertEqual(node.to_html(), "<div ></div>")

if __name__ == '__main__':
    unittest.main()