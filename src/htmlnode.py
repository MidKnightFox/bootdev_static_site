class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props is not None and not isinstance(self.props, dict):
            raise TypeError("Incorrect prop type. Please ensure type is a Dictionary")

        if self.props == None or len(self.props) == 0:
            return ""

        else:
            for key, value in self.props.items():
                html += F" {key}: {value}"
            return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"