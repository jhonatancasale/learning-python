from typing import Optional, overload


class Foo:
    def __init__(self, foo_id):
        self.id = foo_id


@overload
def get_foo(foo_id: None) -> None:
    pass


@overload
def get_foo(foo_id: int) -> Foo:
    pass


def get_foo(foo_id: Optional[int] = None) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)


reveal_type(get_foo(None))
reveal_type(get_foo(5))
