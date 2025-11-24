from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    new_node = TextNode("Anchor Text", TextType.LINK, "https://www.boot.dev")
    print(new_node)

if __name__ == "__main__":
    main()