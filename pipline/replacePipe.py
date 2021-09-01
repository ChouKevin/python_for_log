
from abc import abstractmethod
from pipline.step import Step


class ReplacePipe(Step):
    def __init__(self, regex: str) -> None:
        self.regex = regex

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, regex: {self.regex}'

    @abstractmethod
    def replace(line: str) -> str:
        return NotImplemented

    def handle(self, line: str) -> str:
        return self.replace(line)