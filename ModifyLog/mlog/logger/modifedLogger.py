import time
import json

# Maintainer: nguyenbku97@gmail.com

# logging level
INFO        = 1
WARN        = 2
ERROR       = 3
DEBUG         = 4

# colors mapping
_colorMapping = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "purple": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
}

# styling mapping
BOLD        = 10
ITALIC      = 11
UNDERLINE   = 12

_stylingMapping = {
    BOLD        : "\033[1m",
    ITALIC      : "\033[3m",
    UNDERLINE   : "\033[4m",
}

# level logging mapping 
_levelMapping = {
    INFO        : '[INFO] ',
    WARN        : '[WARN] ',
    ERROR       : '[ERROR]',
    DEBUG       : '[DEBUG]',
}
_formatReset = "\u001b[0m"

def _timeonly() -> str:
    ''' Wrapper on ascitime, to get only time. '''
    return time.asctime().split()[3]

def expStrColor(text: str= "", color: str= "red"):
    ''' Export string with designated color '''
    msg = f"{_colorMapping[color]}{text}{_formatReset}"
    return msg

# Logging Level Methods
def expInfo(text: str= ""):
    ''' Print out text with INFO signal, green color '''
    msg = f"{_colorMapping['green']}[{_timeonly()}] - {_levelMapping[INFO]}: {text}{_formatReset}"
    print(msg)

def expWarn(text: str= ""):
    ''' Print out text with WARN signal, yellow color '''
    msg = f"{_colorMapping['yellow']}[{_timeonly()}] - {_levelMapping[WARN]}: {text}{_formatReset}"
    print(msg)

def expError(text: str= ""):
    ''' Print out text with ERROR signal, red color '''
    msg = f"{_colorMapping['red']}[{_timeonly()}] - {_levelMapping[ERROR]}: {text}{_formatReset}"
    print(msg)

def expDebug(text: str= ""):
    ''' Print out text with DEBUG signal, cyan color '''
    msg = f"{_colorMapping['cyan']}[{_timeonly()}] - {_levelMapping[DEBUG]}: {text}{_formatReset}"
    print(msg)

def expColor(text: str= "", color: str= "white"):
    ''' Print out text with designated color, default is white '''
    msg = expStrColor(text=text, color=color)
    print(msg)

# Styling Methods
def expStyle(text: str= "", format: int = BOLD):
    ''' Print out text with designated styling format, default is 'bold' '''   
    msg = f"{_stylingMapping[format]}{text}{_formatReset}"
    expColor(msg)

def expBold(text: str= ""):
    ''' Print out text with BOLD format '''
    return expStyle(text, format=BOLD)

def expUnderline(text: str= ""):
    ''' Print out text with UNDERLINE format '''
    return expStyle(text, format=UNDERLINE)

def expItalic(text: str= ""):
    ''' Print out text with ITALIC format '''
    return expStyle(text, format=ITALIC)

# Helper Methods
def getColor():
    ''' Print out list of supported colors '''
    lst_color = list()
    for color in _colorMapping:
        lst_color.append(color)
    
    expColor(lst_color, color="purple")

