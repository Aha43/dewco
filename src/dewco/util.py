import numbers

def get_api_value_type(v):
    if (v == None):
        return "null"
    if (isinstance(v, bool)):
        return "boolean"
    if (isinstance(v, numbers.Number)):
        return "number"
    return "string"