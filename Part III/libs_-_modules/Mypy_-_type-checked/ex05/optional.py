from typing import Optional


class Foo:
    def __init__(self, foo_id):
        self.id = foo_id


def get_foo(foo_id: Optional[int] = None) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)


my_foo = get_foo(3)
my_foo.id

my_foo = get_foo()
my_foo.id
