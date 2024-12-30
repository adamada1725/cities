import time
from typing import List, Literal, Self, Tuple, Union

import sys
import os

os.system("")

w = sys.stdout.write
e = "\x1b["

class Point:

    instances = dict() 

    def __new__(cls, x, y):
        return cls.instances.setdefault((x, y), super().__new__(cls))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index: Literal["x", "y"]):
        if index == 0 or index == "x":
            return self.x
        elif index == 1 or index == "y":
            return self.y
        else:
            raise IndexError("Supports only \"0\" (\"x\") or \"1\" (\"y\") indexes")
    
    def __repr__(self):
        return (self.x, self.y)
    
    def __str__(self):
        return str(self.__repr__())

class Style:
    
    def __init__(self, 
                 border: str = "", 
                 background: str = "",
                 padding: int = 0):

        if len(border)>1: raise ValueError("Supports only a single character")
        self.padding = 1 if border and not padding else padding
        self.border = border
        self.background = background

class GUIElement:

    def __init__(self,
                 size: Tuple[int, int] = None,
                 position: Union[Point, Tuple[int, int]] = None,
                 parent: "GUIElement" = None,
                 style: Style = None,
                 display: Literal["block", "inline"] = "block"):

        self.parent: GUIElement = parent
        self.children: List[GUIElement] = []
        self.size: Tuple[int, int] = size
        self.position: Point = Point(*position) if isinstance(position, tuple) else position
        self.style: Style = style
        if style:
            self.size = (size[0]+style.padding*2, size[1]+style.padding*2)
        self.display = display
    
    def render(self):
        s_p = lambda x,y: f"{e}{y};{x}H"
        _str = ""
        if self.style: p = self.style.padding
        else: p = 0
        if self.style and self.style.border:
            w(s_p(self.position.x, self.position.y))
            w(self.style.border*self.size[0])
            for i in range(self.size[1]):
                w(s_p(self.position.x, self.position.y+i))
                w(self.style.border)
                w(s_p(self.position.x+self.size[0]-1, self.position.y+i))
                w(self.style.border)
            w(s_p(self.position.x, self.position.y+self.size[1]))
            w(self.style.border*self.size[0])

        _str+=s_p(self.position.x+p, self.position.y+p)
        _str+=f"{self.__str__()}"
        if self.style:
            if self.style.background:
                _str=self.style.background+_str+f"{e}0m"
        elif self.parent.style:
            if self.parent.style.background:
                _str=self.parent.style.background+_str+f"{e}0m"
        w(_str)
        for c in self.children:
            c.render()

    @staticmethod
    def empty_space_r(element: "GUIElement"):
        
        return element.parent.size[0]-element.size[0]-element.position.x

    def pack(self, element: "GUIElement") -> None:

        if self.children:
            l_c = last_child = self.children[-1]
            if self.empty_space_r(l_c) > element.size[0]:
                element.position = Point(l_c.position.x+l_c.size[0]+1, 
                                         l_c.position.y+l_c.size[1])
            else:
                element.position = Point(0, l_c.position.y+1)
        else:
            element.position = self.position


    def add_element(self, element: "GUIElement") -> Self:
        element.parent = self
        if not element.position: self.pack(element)
        self.children.append(element)
        return self

class Window(GUIElement):

    def __init__(self, size: Tuple[int, int], style: Style = None):
        super().__init__(size=size, position=(0, 0), parent=None, style=style)
    
    def __str__(self):
        return "\n".join([(" "*self.size[0])]*self.size[1])

    def render(self):
        w(f"{e}2J")
        w(f"{e}H")
        return super().render()

class Text(GUIElement):
    
    def __init__(self, text: str, *args, **kwargs):
        kwargs['size'] = (len(text), text.count("\n"))
        super().__init__(*args, **kwargs)
        self.text = text
    
    def __str__(self) -> str:
        if self.empty_space_r(self) < 3:
            return self.text[:self.empty_space_r(self)-3]+"..."
        else:
            return self.text
    
    def render(self):

        return super().render()


red_bg = Style(background=f"{e}41m", border="*")
green_bg = Style(background=f"{e}42m")
root = Window((80, 40), style=red_bg)

t1 = Text("HI!!!!!", position=Point(12, 2))
t2 = Text("Filius dei unicum", style=green_bg)
t3 = Text("\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit")
t4 = Text("\nTestovoe")

root.add_element(t1).add_element(t2).add_element(t3).add_element(t4)


w(f"{e}2J")
w(f"{e}H")
os.system("cls")
root.render()
print(root.size)