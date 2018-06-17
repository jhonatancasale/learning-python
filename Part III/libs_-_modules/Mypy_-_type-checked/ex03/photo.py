from typing import Tuple, List

class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        #self.tags = [] # photo.py:7: error: Need type annotation for variable
        self.tags: List[str] = []

    def get_dimensions(self) -> Tuple[int, int]:
        return (self.width, self.height)
