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