class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def __eq__(self, other_node):
        return (
            self.tag == other_node.tag and
            self.value == other_node.value and
            self.children == other_node.children and
            self.props == other_node.props
        )

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, props=props)
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, props=props)
        self.children = children

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        result = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
