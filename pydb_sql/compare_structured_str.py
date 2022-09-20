import sys

def contain(target, search_word):
    if type(target) is list:
        for t in target:
            if contain(t, search_word):
                return True
        return False
    
    if type(target) is tuple:
        for t in target:
            if contain(t, search_word):
                return True
        return False
    
    if type(target) is not str:
        print('compare_structured_str: contain() gets unexpected data type.', file=sys.stderr)
        return False

    if search_word in target:
        return True
    
    return False

