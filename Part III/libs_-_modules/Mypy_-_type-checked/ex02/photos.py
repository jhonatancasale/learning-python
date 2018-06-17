from typing import Tuple

class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_dimensions(self) -> Tuple[int, int]:
        return (self.width, self.height)


photos = [
    Photo(640, 480),
    Photo(1024, 768)
]

photos.append('foo')
