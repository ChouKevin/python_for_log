
import re
from typing import Optional
from .step import Step


class Search(Step):
    """if match(or not) the regex, then pass the line """
    def __init__(self, pattern: str, block_if_match: bool = False) -> None:
        self.pattern = pattern
        self.block_if_match = block_if_match

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, regex: {self.pattern}'

    def handle(self, line: str) -> str:
        match_part = re.search(self.pattern, line)
        if self.block_if_match:
            return "" if match_part is not None else line
        else:
            return line if match_part is not None else ""
