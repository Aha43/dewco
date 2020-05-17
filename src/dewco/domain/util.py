# Domain types attributes are all strings. Here is functions used to convert from other types to Domain attributes and vice versa. 
# Functions here should only be used for the above stated purpose.

from typing import List

def str_to_bool(v: str) -> bool:
    if v:
        if v.lower() == "true":
            return True
    return False

def str_to_int(v: str) -> int:
    if v:
        return int(v)
    return int()

def str_to_int_list(v: str) -> List[int]:
    retVal = []
    if v:
        split = v.split(",")
        for e in split:
            retVal.append(int(e))
    return retVal

def list_to_str(l: []) -> str:
    retVal = ""
    for e in l:
        retVal = retVal + str(e) + ","
    return retVal

def str_to_float(v: str) -> float:
    if v:
        return float(v)
    return float()

def object_to_str(o: object) -> str:
    if o == None:
        return ""
    s = str(o)
    l = s.lower()
    if l == "false" or l == "true":
        return l
    return s

def get_dict_value(name: str, dict, default: str = "") -> str:
    if name in dict:
        return object_to_str(dict[name])
    return default
