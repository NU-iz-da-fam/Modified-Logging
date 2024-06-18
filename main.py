import mlog

if __name__ == "__main__":
    mlog.expInfo("Main Application")

    # mlog info
    mlog.expBold(mlog.__version__)
    mlog.expItalic(mlog.__author__)
    mlog.expUnderline(mlog.__date__)

    # Level name
    mlog.getLevelName()

    # Format name 
    mlog.getFormatName()

    # Styling Name
    mlog.getColorName()
    
