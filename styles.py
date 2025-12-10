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
    default = 7,
    black   = 40,
    red     = 41,
    green   = 42,
    yellow  = 43,
    blue    = 44,
    purple  = 45,
    cyan    = 46,
    white   = 47,

    light_black     = 100,
    light_red       = 101,
    light_green     = 102,
    light_yellow    = 103,
    light_blue      = 104,
    light_purple    = 105,
    light_cyan      = 106,
    light_white     = 107
# end of the class

def __code(code: int = 0) -> str:
    return f'\x1b[{code}m'

def add_style(_text: str, *_styles: int) -> str:
    addition = ''
    
    # adding the styles of text
    for i in _styles:
        addition += __code(i)

    return addition + _text + __code(0)

cd = __code
add = add_style

print(f'{cd(select.light_red)}Ещё одна проверка работоспособности{cd(0)}')
