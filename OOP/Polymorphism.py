from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class DropDownlist(UIControl):
    def draw(self):
        print("DropDownlist")


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


def draw(controls):  # didn't know which draw it working with. Only determine in run time
    for control in controls:
        control.draw()


ddl = DropDownlist()
textBox = TextBox()
draw([ddl, textBox])

# duck Typing


class DropDownlist:
    def draw(self):
        print("DropDownlist")


class TextBox:
    def draw(self):
        print("TextBox")


def draw(controls):
    for control in controls:
        control.draw()  # only look for draw()


ddl = DropDownlist()
textBox = TextBox()
draw([ddl, textBox])
