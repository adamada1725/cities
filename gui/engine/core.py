from abc import ABC, abstractmethod
from typing import Optional, TypeVar

class BaseANSIElement(ABC):

    def __init__(self, str: str):
        self.str = str

    def __str__(self):
        return self.str
 
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, value):
        return self.__str__()+value
    
    def __radd__(self, value):
        return self.__add__(value)

A = TypeVar("A", bound=BaseANSIElement)


class _Common(BaseANSIElement):
    pass

class Commons:
    ESC = _Common("\x1b")
    ESC_ = _Common("\x1b[")
    RESET = _Common(f"{ESC_}0m")

class Tag:
    def __init__(self,
                 element: A,
                 str: str):
        self.element = element
        self.str = str

class _Tagable(ABC, _Common):

    def __init__(self, _open: Tag, _close: Optional[Tag], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._open = _open
        self._close = _close

class _Valuable(ABC):
        
        @abstractmethod
        def __init__(self, value):
            self.value = value

class _Style(_Common, _Valuable, _Tagable):

    def __init__(self, value: int):
        super().__init__()
        self.value = value
        self.str = f"\x1b[{value}m"

a = _Style()

class _Color(_Common, _Valuable, _Tagable):
    def __init__(self, value):
        self.value = value
        self.str = f"\x1b[{value}m"

class _Background(_Common, _Valuable, _Tagable):
    def __init__(self, value):
        self.value = value
        self.str = f"\x1b[{value}m"


class Styles:
    S = _Style
    BOLD = S(1)
    FAINT = S(2)
    ITALIC = S(3)
    UNDERLINE = S(4)
    BLINKING = S(5)
    INVERSE = S(7)
    HIDDEN = S(8)
    RESET = S(0)
    STRIKETHROUGH = S(9)

class Colors:
    C = _Color
    BLACK = C(30)
    RED = C(31)
    GREEN = C(32)
    YELLOW = C(33)
    BLUE = C(34)
    MAGENTA = C(35)
    CYAN = C(36)
    WHITE = C(37)
    DEF_COLOR = C(39)

class Background:
    B = _Background
    BLACK = B(40)
    RED = B(41)
    GREEN = B(42)
    YELLOW = B(43)
    BLUE = B(44)
    MAGENTA = B(45)
    CYAN = B(46)
    WHITE = B(47)
    DEF_COLOR = B(49)

class Format:

    @staticmethod
    def format(style: _Style = None,
               color: _Color = None,
               background: _Background = None):

        return Commons.ESC_+";".join(
            (list
            (map(lambda x: str(x.value), 
                filter(lambda x: True if x!=None else False, 
                        [style, color, background]
                        )
                )
            )
            )
        )+"m"

    @staticmethod
    def format_text(text: str,
                    style: _Style = None,
                    color: _Color = None,
                    background: _Background = None):
        return format(style, color, background)+text+Commons.RESET

    def __init__(self,
                 style: _Style = None, 
                 color: _Color = None, 
                 background: _Background = None):
        
        self.style = style
        self.color = color
        self.background = background
    
    def __str__(self):
        return self.format(self.style, self.color, self.background)

class Text:
    
    class Tags:
        pass
        

    def __analyze():
        pass

    class __Fragment:
        def __init__(self, str: str, format: Format):
            

    def __init__(self, str: str):
        pass

