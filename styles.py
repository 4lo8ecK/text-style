import sys

def cls() -> None:
    sys.stdout.write('\x1bc')

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
# end of the class
class color:
    default = 0
    black   = 30
    red     = 31
    green   = 32
    yellow  = 33
    blue    = 34
    purple  = 35
    cyan    = 36
    
    light_black     = 90
    light_red       = 91
    light_green     = 92
    light_yellow    = 93
    light_blue      = 94
    light_purple    = 95
    light_cyan      = 96

    light_white     = 97
# end of the class
class select:
    default: int = 7
    black: int   = 40
    red: int     = 41
    green: int   = 42
    yellow: int  = 43
    blue: int    = 44
    purple: int  = 45
    cyan: int    = 46
    white: int   = 47

    grey: int           = 100
    light_red: int      = 101
    light_green: int    = 102
    light_yellow: int   = 103
    light_blue: int     = 104
    light_purple: int   = 105
    light_cyan: int     = 106
    light_white: int    = 107
# end of the class

def cd(code: int = 0) -> str:
    return f'\x1b[{code}m'

def add(_text: str, *_styles: int) -> str:
    addition = ''
    # adding the styles of text
    for i in _styles:
        addition += cd(i)
    return addition + _text + cd(0)

def rgb(red: int = 0, green: int = 0, blue: int = 0) -> str:
    if red > 255: red = 255
    elif red < 0: red = 0

    if green > 255: green = 255
    elif green < 0: green = 0

    if blue > 255: blue = 255
    elif blue < 0: blue = 0

    return f'\x1b[38;2;{red};{green};{blue}m'

# def add_rgb(text: str, *colors: int) -> str:
    
#     pass

print(f'{rgb(255, 150, 50)}Text{cd(0)}')