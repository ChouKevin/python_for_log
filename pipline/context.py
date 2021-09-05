
from pipline.step import Step
from typing import Iterable


class Context:
    def __init__(self, steps: Iterable[Step] = []) -> None:
        self.steps = steps

    def exec(self, lines: Iterable[Step] = []) -> None:
        for line in lines:
            for step in self.steps:
                line = step.handle(line)
        self._finish()

    def _finish(self):
        for step in self.steps:
            step.finish()
