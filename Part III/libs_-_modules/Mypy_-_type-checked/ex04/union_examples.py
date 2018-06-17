from typing import Union, Optional

class Foo:
    pass

class Bar:
    pass


def get_foo_or_bar(id: int) -> Union[Foo, Bar]:
    pass

def get_foo_or_none(id: int) -> Union[Foo, None]:
    pass

def get_foo_or_none2(id: int) -> Optional[Foo]:
    pass
