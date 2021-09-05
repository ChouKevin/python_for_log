import os
from typing import Optional
from .step import Step

class Write(Step):
    def __init__(self, path: str) -> None:
        self.path = path
        self._preprocess(path)
        self.file = open(path, 'a+')

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, path: {self.path}'

    def _preprocess(self, path: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            os.remove(path)

    def handle(self, line: str) -> str:
        if line and line.strip():
            self.file.write(line)
        return line

    def finish(self):
        self.file.close()