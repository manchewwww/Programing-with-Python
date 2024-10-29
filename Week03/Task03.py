class Spacer:
    def __init__(self, length=1):
        self.length = length

    def render(self):
        return self.length * " "


class Line:
    def __init__(self, length, symbol="-"):
        self.length = length
        self.symbol = symbol

    def render(self):
        return f"{self.symbol}" * self.length


class Text:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class FancyText:
    def __init__(self, text, symbol="="):
        self.text = text
        self.symbol = symbol

    def render(self):
        return f"{self.symbol}{self.symbol.join(i for i in self.text)}{self.symbol}"


class HorizontalStack:
    def __init__(self, *elements):
        self.elements = elements

    def render(self):
        return "".join(element.render() for element in self.elements)


class VerticalStack:
    def __init__(self, *elements):
        self.elements = elements

    def render(self):
        return "\n".join(element.render() for element in self.elements)


class Box:
    def __init__(self, width, *elements):
        self.width = width
        self.elements = elements

    def render(self):
        border = HorizontalStack(Text("+"), Line(self.width - 2, symbol="="), Text("+"))

        box_content = [border.render()]

        for el in self.elements:
            content = f"|{el.render()}"

            if len(content) > self.width:
                content = content[: self.width - 1]
            elif len(content) < self.width:
                content += Spacer(self.width - len(content) - 1).render()

            box_content.append(f"{content}|")

        # box_content += [f"|{el.render()}|" if len(el=el.) for el in self.elements]
        box_content += [border.render()]
        return "\n".join(box_content)


class ProgressBar:
    def __init__(self, length, progress):
        self.length = length
        self.progress = progress

    def render(self):
        count = int(self.length * self.progress)
        return f"[{"=" * count}{"-" * (self.length - count - 2)}]"


ui = Box(
    19,
    FancyText("WELCOME!"),
    Spacer(),
    Text("Loading packages:THIS SHOULD NOT BE SHOWN IN THE BOX"),
    HorizontalStack(Line(3), Spacer(), Text("cowsay")),
    HorizontalStack(Line(3), Spacer(), Text("lolcat")),
    HorizontalStack(Line(3, symbol=">"), Spacer(), Text("whoami"), Text("...")),
    Spacer(),
    HorizontalStack(Spacer(), ProgressBar(15, 0.4), Spacer()),
)

print(ui.render())
