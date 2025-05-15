class HTMLNode:
    # set the arguements with fefault values to set them as optional
    # to make them "Mandatory" then just ommit the defined value
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
            #Unpack each key:value pair into a specified format then append to the 'html' string
            for key, value in self.props.items():
                html += f" {key}: {value}"
            return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    #tag and value are mandatory, props is optional as it's been provided a value
    def __init__(self,tag,value,props={}): 
        # assigning values to pass to parent class. 
        # this method sets the parent (left) by keyword. the right side is the local set in the local constructor.
            # another method is to just set it positionally (match the arguement position to that of the parent)
        # children=[] sets an empty list to be passed through as the value so no other child can be created.
            #this effectivly blocks it from being defined.
        super().__init__(tag=tag,value=value,children=[],props=props)  

    def to_html(self):
        #need to add self to the method for it to refernce the class it belongs to properly

        ## Raise error if no value provided
        if self.value is None:
            raise ValueError("Leafnode must have a VALUE")

        ## if no tag provided then return the value without modification (raw text)
        if self.tag is None:
            return self.value

        ## unpack all props in standard format
        prop_text = ""
        for prop_key,prop_value in self.props.items():
            prop_text += f' {prop_key}="{prop_value}"'

        return (f"<{self.tag}{prop_text}>{self.value}</{self.tag}>")

class ParentNode(HTMLNode):
    pass
        