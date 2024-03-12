class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False
        elif self.text_type != other.text_type:
            return False
        elif self.url != other.url:
            return False
        else:
            return True

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
