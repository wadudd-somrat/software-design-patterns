# Step 1: Create a text component interface (or abstract class)
from abc import ABC, abstractmethod

class TextComponent(ABC):
    @abstractmethod
    def render(self):
        pass

# Step 2: Create a concrete text component class
class PlainText(TextComponent):
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

# Step 3: Create decorator classes that extend the text component
class BoldDecorator(TextComponent):
    def __init__(self, text_component):
        self._text_component = text_component

    def render(self):
        return f"<b>{self._text_component.render()}</b>"

class ItalicDecorator(TextComponent):
    def __init__(self, text_component):
        self._text_component = text_component

    def render(self):
        return f"<i>{self._text_component.render()}</i>"

# Step 4: Client code
if __name__ == "__main__":
    plain_text = PlainText("Hello, World!")

    bold_text = BoldDecorator(plain_text)
    italic_text = ItalicDecorator(plain_text)
    bold_italic_text = BoldDecorator(italic_text)

    print("Plain Text: " + plain_text.render())
    print("Bold Text: " + bold_text.render())
    print("Italic Text: " + italic_text.render())
    print("Bold and Italic Text: " + bold_italic_text.render())