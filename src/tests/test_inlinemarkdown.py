import unittest
from src.inlinemarkdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from src.textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](http://example.com/image.jpg)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [("alt text", "http://example.com/image.jpg")],
            images,
        )

    def test_extract_markdown_images_multiple(self):
        text = "First image ![first](http://example.com/first.jpg) and second image ![second](http://example.com/second.jpg)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("first", "http://example.com/first.jpg"),
                ("second", "http://example.com/second.jpg"),
            ],
            images,
        )

    def test_extract_markdown_links(self):
        text = "Here is a [link](http://example.com)"
        links = extract_markdown_links(text)
        self.assertListEqual(
        [("link", "http://example.com")],
        links,
        )

def test_extract_markdown_links_multiple(self):
        text = "First [link](http://example.com/first) and second [link](http://example.com/second)"
        links = extract_markdown_links(text)
        self.assertListEqual(
        [
            ("link", "http://example.com/first"),
            ("link", "http://example.com/second"),
        ],
            links,
        )

    

if __name__ == "__main__":
    unittest.main()
