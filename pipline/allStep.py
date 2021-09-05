from typing import Iterable, Optional
from .step import Step

class AllStep(Step):
    def __init__(self, steps: Iterable[Step] = []) -> None:
        self.steps = steps

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, ' + ' '.join([str(step) for step in self.steps])

    def handle(self, line: str) -> str:
        for step in self.steps:
            line = step.handle(line)
            if not line or line.isspace():
                break
        return line

    def finish(self):
        for step in self.steps:
            step.finish()