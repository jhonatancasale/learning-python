from typing import Tuple

class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_dimensions(self) -> Tuple[str, str]:
        return (self.width, self.height)
