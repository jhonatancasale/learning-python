from typing import TypeVar

AnyStr = TypeVar('AnyStr', str, bytes)

def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat('foo', b'bar') # generic_functions.py:8: error: Value of type variable "AnyStr" of "concat" cannot be "object"
concat(3, 6) # generic_functions.py:9: error: Value of type variable "AnyStr" of "concat" cannot be "int"
reveal_type(concat('foo', 'bar')) # generic_functions.py:10: error: Revealed type is 'builtins.str*'
reveal_type(concat(b'foo', b'bar')) # generic_functions.py:11: error: Revealed type is 'builtins.bytes*'

