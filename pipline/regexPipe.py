
import re
from typing import Optional
from .step import Step


class RegexPipe(Step):
    """if match(or not) the regex, then pass the line """
    def __init__(self, regex: str, block_if_match: bool = False) -> None:
        self.regex = regex
        self.block_if_match = block_if_match

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, regex: {self.regex}'

    def handle(self, line: str) -> str:
        match_part = re.search(self.regex, line)
        if self.block_if_match:
            return "" if match_part is not None else line
        else:
            return line if match_part is not None else ""
