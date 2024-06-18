import mlog
from typing import List, Union
# Maintainer: nguyenbku97@gmail.com

def inputCondition(msg: str = "", accept = Union[List[str], str], retry: int = 5):
    ''' 
        Input from console with specific condition 
        @param msg: message to print out
        @param accept: inputs that are ok
        @param retry: number of retry 
    '''
    msg = mlog.expStrColor(f"{msg}: ( accept: {accept} )", color= 'green', level= mlog.INFO)
    count = 0
    while True:
        answer = input(f"{msg}: ").lower()
        condition = False
        try:
            condition =  bool(answer in accept)
        except:
            condition =  bool(answer == accept)
        
        if condition:
            break
        count += 1
        if count > retry:
            raise Exception('Exceed limit number')
        mlog.expWarn('Invalid Input. Please try again!')

