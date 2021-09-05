
from abc import abstractmethod
from pipline.step import Step


class Replace(Step):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, regex: {self.pattern}'

    @abstractmethod
    def replace(line: str) -> str:
        return NotImplemented

    def handle(self, line: str) -> str:
        return self.replace(line)