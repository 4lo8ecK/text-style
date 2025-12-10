import sys

def cls() -> None:
    sys.stdout.write('\x1bc')

class styles:
    _COLORS = {
        'default':  0,
        'black':    30,
        'red':      31,
        'green':    32,
        'yellow':   33,
        'blue':     34,
        'purple':   35,
        'cyan':     36,

        'light black':    90,
        'light red':      91,
        'light green':    92,
        'light yellow':   93,
        'light blue':     94,
        'light purple':   95,
        'light cyan':     96,
        'light white':    97
    }  
    _SELECTION = {
        'default':  7,
        'black':    40,
        'red':      41,
        'green':    42,
        'yellow':   43,
        'blue':     44,
        'purple':   45,
        'cyan':     46,
        'white':    47,

        'light black':    100,
        'light red':      101,
        'light green':    102,
        'light yellow':   103,
        'light blue':     104,
        'light purple':   105,
        'light cyan':     106,
        'light white':    107

    }
    _FONT_STYLE = {
        'default':      0,
        'bold':         1,
        'dim':          2,
        'italic':       3,
        'underline':    4,
        'blink':        5,
        'fast blink':   6,
        'reverse':      7,
        'hidden':       8,
        'cross':        9,
        'double underline': 21,
        'thin underline':   52
    }

    @staticmethod
    def _code(code: int = 0) -> str:
        return f'\x1b[{code}m'
    
    @staticmethod
    def _int_add_style(
            string: str,
            *style: int | str,
            color: int | str = None,
            selection: int | str = None
    ) -> str:
        res = ''
        vals = styles._FONT_STYLE.values()
        for i in style:
            if i in vals:
                res += styles._code(i)

        if color != None and color != 0:
            res += styles._code(color)

        if selection != None and selection != 0:
            res += styles._code(selection)

        return res + string + styles._code(0)

    @staticmethod
    def _str_add_style(
            string: str,
            *style: str,
            color: str | None = None,
            selection: str | None = None
    ) -> str:
        res = ''
        font_styles = styles._FONT_STYLE.keys()
        for i in style:
            if i in font_styles:
                val = styles._FONT_STYLE.get(i)
                res += styles._code(val)
        del font_styles

        if (color != None) or (color != 'default'):
            if color in styles._COLORS.keys():
                val = styles._COLORS.get(color)
                res += styles._code(val)
        
        if selection != None:
            if selection in styles._SELECTION.keys():
                val = styles._SELECTION.get(selection)
                res += styles._code(val)
        
        return res + string + styles._code(0)

    @staticmethod
    def add_style(
        string: str, *style: int | str,
        color: int | str = None, selection: int | str = None
    ) -> str:
        if all(isinstance(arg, int) for arg in style):
            if (isinstance(color, int) or color == None) \
                and (isinstance(selection, int) or selection == None):
                return styles._int_add_style(string, *style, color=color, selection=selection)
        
        elif all(isinstance(arg, str) for arg in style):
            if (isinstance(color, str) or color == None) \
                and (isinstance(selection, str) or selection == None):
                return styles._str_add_style(string, *style, color=color, selection=selection)
        return string


#region USELESS MAYBE WILL BE DELETED
# #region FUNCTIONS
# def code(code: int = 0) -> str:
#     return f'\x1b[{code}m'

# def cls() -> None:
#     print('\x1bc', end='')

# def _int_add_styles(*codes: int, line: str) -> str:
#     res = ''
#     for i in codes:
#         res += code(i)
#     res += (line + '\x1b[0m')
#     return res

# def _str_add_styles(*codes: str, line: str) -> str:
#     res = ''
#     for i in codes:
#         res += i
#     res += (line + '\x1b[0m')
#     return res

# def add_styles(*codes: int | str, line: str) -> str:
#     if all(isinstance(arg, int) for arg in codes):
#         return _int_add_styles(*codes, line=line)
    
#     elif all(isinstance(arg, str) for arg in codes):
#         return _str_add_styles(*codes, line=line)

#     return line

# #endregion
# # region FONT TAGS
# clearconsole: str =     '\x1bc'
# clear: str =            '\x1bc'  
# end: str =              code(0)
# default: str =          code(0)
# bold: str =             code(1)
# grey: str =             code(2)
# italic: str =           code(3)
# underline: str =        code(4)     
# blink: str =            code(5)
# blink2: str =           code(6)
# select: str =           code(7)
# bselect: str =          code(8)
# cross: str =            code(9)

# double_underline: str = code(21)
# thin_underline: str =   code(52)
# # endregion
# # region COLOR TAGS
# # region default colors 
# black: str =        code(30)    # black font color
# red: str =          code(31)    # red font color
# green: str =        code(32)    # green font color
# yellow: str =       code(33)    # yellow font color
# blue: str =         code(34)    # blue font color
# purple: str =       code(35)    # purple font color
# lightblue: str =    code(36)    # light blue font color
# white: str =        code(37)    
# #endregion

# #region light colors
# light_black: str =      code(90)    # black font color
# light_red: str =        code(91)    # red font color
# light_green: str =      code(92)    # green font color
# light_yellow: str =     code(93)    # yellow font color
# light_blue: str =       code(94)    # blue font color
# light_purple: str =     code(95)    # purple font color
# light_lightblue: str =  code(96)    # light blue font color
# light_white: str =      code(97)    # white font color

# l_black: str =      code(90)    # black font color
# l_red: str =        code(91)    # red font color
# l_green: str =      code(92)    # green font color
# l_yellow: str =     code(93)    # yellow font color
# l_blue: str =       code(94)    # blue font color
# l_purple: str =     code(95)    # purple font color
# l_lightblue: str =  code(96)    # light blue font color
# l_white: str =      code(97)    # white font color
# # endregion
# # endregion
# # region SELECTIONS
# # region default selections
# select_black: str =     code(40)    # black font color
# select_red: str =       code(41)    # red font color
# select_green: str =     code(42)    # green font color
# select_yellow: str =    code(43)    # yellow font color
# select_blue: str =      code(44)    # blue font color
# select_purple: str =    code(45)    # purple font color
# select_lightblue: str = code(46)    # light blue font color
# select_white: str =     code(47)

# s_black: str =     code(40)    # black font color
# s_red: str =       code(41)    # red font color
# s_green: str =     code(42)    # green font color
# s_yellow: str =    code(43)    # yellow font color
# s_blue: str =      code(44)    # blue font color
# s_purple: str =    code(45)    # purple font color
# s_lightblue: str = code(46)    # light blue font color
# s_white: str =     code(47)
# #endregion

# # region light selections
# light_select_black: str =     code(100)    # black font color
# light_select_red: str =       code(101)    # red font color
# light_select_green: str =     code(102)    # green font color
# light_select_yellow: str =    code(103)    # yellow font color
# light_select_blue: str =      code(104)    # blue font color
# light_select_purple: str =    code(105)    # purple font color
# light_select_lightblue: str = code(106)    # light blue font color
# light_select_white: str =     code(107)

# ls_black: str =     code(100)    # black font color
# ls_red: str =       code(101)    # red font color
# ls_green: str =     code(102)    # green font color
# ls_yellow: str =    code(103)    # yellow font color
# ls_blue: str =      code(104)    # blue font color
# ls_purple: str =    code(105)    # purple font color
# ls_lightblue: str = code(106)    # light blue font color
# ls_white: str =     code(107)
# #endregion
# #endregion

#endregion