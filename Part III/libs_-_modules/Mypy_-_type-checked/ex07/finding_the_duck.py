from typing_extensions import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

def render(obj: Renderable) -> str:
    return obj.render()

class Foo:
    def render(self) -> str:
        return 'Foo!'

render(Foo())
render(3) # finding_the_duck.py:14: error: Argument 1 to "render" has incompatible type "int"; expected "Renderable"
