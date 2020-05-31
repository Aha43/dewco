import enum
import numbers
import os


def get_env_var(name: str, default: str = None) -> str:
    retVal = os.getenv(name)
    if retVal == None:
       return default
    return retVal
    
def put_env_var(name: str, val: str) -> None:
    os.putenv(name, val)
    