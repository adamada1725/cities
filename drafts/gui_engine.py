from abc import ABC
import sys

class ANSIElement(str, ABC):

    def __new__(cls, _str, *args, **kwargs):
        return super().__new__(cls, _str)

class Formatted(ANSIElement, ABC):

    def __new__(cls, *values, **kwargs):
        return super().__new__(cls, cls.pattern.format(*values))
    
    def __init__(self, *values):
        self.values = [*values]
    
    def __init_subclass__(cls, pattern: str):
        cls.pattern = pattern

class GraphicsMode(Formatted, pattern="\x1b[{}m"):
    def __init_subclass__(cls, allowable_range: list[int, int]):
        cls.pattern = cls.pattern
        cls.allowable_range = allowable_range
    
    def __new__(cls, *values, **kwargs):
        for v in values:
            if v not in cls.allowable_range:
                raise KeyError("Invalid value (beyond allowable range)")

        return super().__new__(cls, ";".join(map(str, [*values])))
    
    def __add__(self, value):
        if isinstance(value, GraphicsMode):
            self.values+=value.values
            print(self.values)
        return super().__add__(value)

class Style(GraphicsMode, allowable_range = range(1,10)):
    pass

class Color(GraphicsMode, allowable_range = range(30,40)):
    pass

class Background(GraphicsMode, allowable_range = range(40,50)):
    pass

RED = Color(31)
BLACK = Color(30)
RED = Color(31)
GREEN = Color(32)
YELLOW = Color(33)
BLUE = Color(34)
MAGENTA = Color(35)
CYAN = Color(36)
WHITE = Color(37)
DEFAULT = Color(39)

BOLD = Style(1)

sys.stdout.write(BLUE+MAGENTA+CYAN+WHITE+"arasr"+RED+"sarasr")