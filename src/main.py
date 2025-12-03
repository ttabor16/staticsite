from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from refresh import static_to_public

def main():
    #new_node = TextNode("Anchor Text", TextType.LINK, "https://www.boot.dev")
    #print(new_node)
    static_to_public()


if __name__ == "__main__":
    main()