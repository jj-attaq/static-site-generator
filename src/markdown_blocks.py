from htmlnode import (
    LeafNode,
    ParentNode
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not block.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not block.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not block.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph


def convert_paragraph_to_html_node(block):
    return ""


def convert_heading_to_html_node(block):
    # def __init__(self, tag, children, props=None):
    # def __init__(self, tag, value, props=None):
    count = block.count('#', 0, block.find(' '))
    content = content = block.lstrip('# ').strip()
    node = ParentNode(f"h{count}", content)
    return node


def convert_code_to_html_node(block):
    return ""


def convert_quote_to_html_node(block):
    return ""


def convert_ulist_to_html_node(block):
    return ""


def convert_olist_to_html_node(block):
    return ""


def markdown_to_html_node(markdown):
    # That top-level HTMLNode should just be a <div>, where each child is a block of the document. Each block should have its own "inline" children.
    blocks = markdown_to_blocks(markdown)

    def block_types(b):
        block_types = []
        for block in b:
            block_types.append(block_to_block_type(block))
        return block_types

    blocks_and_types = list(zip(blocks, block_types(blocks)))

    for b_and_t in blocks_and_types:
        if b_and_t[1] == block_type_paragraph:
            convert_paragraph_to_html_node(b_and_t[0])
        if b_and_t[1] == block_type_heading:
            convert_heading_to_html_node(b_and_t[0])
        if b_and_t[1] == block_type_code:
            convert_code_to_html_node(b_and_t[0])
        if b_and_t[1] == block_type_quote:
            convert_quote_to_html_node(b_and_t[0])
        if b_and_t[1] == block_type_ulist:
            convert_ulist_to_html_node(b_and_t[0])
        if b_and_t[1] == block_type_olist:
            convert_olist_to_html_node(b_and_t[0])
