import sys
import os
os.system("") #нужно для корректной работы ANSI последовательностей в Windows CMD

w = sys.stdout.write

class ANSI:
    
    ESC = "\x1b"
    
    CLEAR_SCREEN = f"{ESC}[2J"
    CLEAR_LINE = f"{ESC}[0J"
    CLEAR_TO_BEGINING = f"{ESC}[1J"

    class Valuable:

        def __init__(self, value, str):
            self.value = value
            self.str = str

        def get_value(self):
            return self.value
        
        def __str__(self):
            return self.str
    
    class _Style(Valuable):
        def __init__(self, value):
            self.value = value
            self.str = f"\x1b[{value}m"

    class _Color(Valuable):
        def __init__(self, value):
            self.value = value
            self.str = f"\x1b[{value}m"

    class _Background(Valuable):
        def __init__(self, value):
            self.value = value
            self.str = f"\x1b[{value}m"
        
    S = _Style

    C = _Color

    RESET = S(0)
    BOLD = S(1)
    FAINT = S(2)
    ITALIC = S(3)
    UNDERLINE = S(4)
    BLINKING = S(5)
    INVERSE = S(7)
    HIDDEN = S(8)
    RESET = S(0)
    STRIKETHROUGH = S(9)

    RESET = C(0)
    RED = C(42)
    

    class CURSOR:
        
        ESC = "\x1b"
        
        SET_HOME = f"{ESC}[H"

        @classmethod
        def SET_POS(cls, x, y):
            return f"{cls.ESC}[{x};{y}H"
        
        @classmethod
        def MV_UP(cls, lines=1):
            return f"{cls.ESC}[{lines}A"
        
        @classmethod
        def MV_DOWN(cls, lines=1):
            return f"{cls.ESC}[{lines}B"
        
        @classmethod
        def MV_NEXT_LINE(cls, lines=1):
            return f"{cls.ESC}[{lines}E"

        @classmethod
        def SET_REL_POS(cls, x,y):
            return f"{cls.ESC}[H{x};{y}H"



if __name__ == "__main__":
    print(ANSI.RED)