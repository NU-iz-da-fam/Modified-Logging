# import sys
# sys.path.append("../")
import modlog as mlog

if __name__ == "__main__":
    # Default white color
    mlog.expColor("Test modify logging library")
    
    # Info level
    mlog.expInfo("Hello World!")

    # Warning level
    mlog.expWarn("Hello World!")

    # Error level
    mlog.expError("Hello World!")

    # Debug level
    mlog.expDebug("Hello World!")

    # Print with color
    mlog.expColor("Blue Hello World! with {}".format("ABC"), color="blue")

    # Print with designated style 
    mlog.expStyle("Style Hello World!")

    # Print with designated style 
    mlog.expBold("Bold Hello World!")

    # Print with designated style 
    mlog.expItalic("Italic Hello World!")

    # Print with designated style 
    mlog.expUnderline("Underline Hello World!")

    # Get color list
    mlog.getColor()