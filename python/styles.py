import sys
import time

# region global methods
def cls() -> None:
    sys.stdout.write('\x1bc')

def cd(code: int = 0) -> str:
    return f'\x1b[{code}m'

def add(_text: str, *_styles: int) -> str:
    addition = ''
    # adding the styles of text
    for i in _styles:
        addition += cd(i)
    return addition + _text + cd(0)
# endregion

class rgb:
    @staticmethod
    def cd(r: int = 255, g: int = 255, b: int = 255) -> str:
        return f'\x1b[38;2;{r};{g};{b}m'

    @staticmethod
    def clamp(value: int, min: int = 0, max: int = 255) -> int:
        if value < min: value = min
        elif value > max: value = max
        return value
    
    def __init__(self, r: int = 255, g: int = 255, b: int = 255):
        self.r = self.clamp(value=r)
        self.g = self.clamp(value=g)
        self.b = self.clamp(value=b)

    def __call__(self, *args, **kwds):
        return self.fg()

    def __str__(self) -> str:
        return self.fg()
    
    def fg(self) -> str:
        return f'\x1b[38;2;{self.r};{self.g};{self.b}m'
    def bg(self) -> str:
        return f'\x1b[48;2;{self.r};{self.g};{self.b}m'

class color(rgb):
    class light(rgb):
        black = rgb(118, 118, 118)
        red = rgb(231, 72, 86)
        green = rgb(22, 198, 12)
        yellow = rgb(249, 241, 165)
        blue = rgb(59, 120, 255)
        purple = rgb(180, 0, 158)
        cyan = rgb(97, 214, 214)
        white = rgb(242, 242, 242)
    black = rgb(12, 12, 12)
    red = rgb(197, 15, 31)
    green = rgb(19, 161, 14)
    yellow = rgb(193, 156, 0)
    blue = rgb(0, 55, 218)
    purple = rgb(136, 23, 152)
    cyan = rgb(58, 150, 221)
    white = rgb(204, 204, 204)

    class style:
        default     = 0
        bold        = 1
        dim         = 2
        italic      = 3
        underline   = 4
        blink       = 5
        fast_blink  = 6
        reverse     = 7
        hidden      = 8
        cross       = 9
        double_underline = 21
        thin_underline = 52
    class color:
        class light:
            default = 90
            black   = 90
            red     = 91
            green   = 92
            yellow  = 93
            blue    = 94
            purple  = 95
            cyan    = 96
            white   = 97

        default = 0
        black   = 30
        red     = 31
        green   = 32
        yellow  = 33
        blue    = 34
        purple  = 35
        cyan    = 36
    class select:
        class light:
            black: int   = 100
            red: int     = 101
            green: int   = 102
            yellow: int  = 103
            blue: int    = 104
            purple: int  = 105
            cyan: int    = 106
            white: int   = 107
        default: int = 7
        black: int   = 40
        red: int     = 41
        green: int   = 42
        yellow: int  = 43
        blue: int    = 44
        purple: int  = 45
        cyan: int    = 46
        white: int   = 47

print(f'{cd(color.color.blue)}Text{cd(0)}')
