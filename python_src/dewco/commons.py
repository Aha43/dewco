
# Strings starts
def is_null_or_empty(s: str) -> bool:
    if s is None:
        return True
    if len(s.strip()) == 0:
        return True
    return False
# Strings ends

# Exceptions starts
class Raise:
    @staticmethod
    def if_none_or_empty_str(v: str, name: str = None) -> None:
        Raise.if_none_reference(v, name)
        v = v.strip()
        if len(str) == 0:
            raise ValueError(Raise.__add_name("Empty str", name))
    
    @staticmethod
    def if_none_reference(v, name: str = None) -> None:
        if v == None:
            raise ValueError(Raise.__add_name("None reference", name))
    
    @staticmethod
    def if_not_of_length(l, n: int, name: str = None) -> None:
        Raise.if_none_reference(l, name)
        if len(l) != n:
            raise ValueError(Raise.__add_name("not of length " + str(n), name))

    @staticmethod
    def if_not_in_range(v, start, to, name: str = None) -> None:
        if v < start:
            raise ValueError(Raise.__add_name("< " + str(start), name))
        if v >= to:
            raise ValueError(Raise.__add_name(">= " + str(start), name))

    @staticmethod
    def __add_name(msg: str, name: str) -> str:
        if not is_null_or_empty(name):
            msg += " : " + name.strip()
        return msg
# Exceptions ends
