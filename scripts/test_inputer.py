import mlog

if __name__ == "__main__":
    mlog.expInfo("Test Inputer")

    # Input with condition
    mlog.inputCondition('Press Q to quit', ['q','a'], 3)
