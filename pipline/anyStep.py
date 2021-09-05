from typing import Iterable
from .step import Step

class AnyStep(Step) :
    """ if there was one step can handle the log, then return the first result
        otherwise return empty
    """
    def __init__(self, steps: Iterable[Step] = []) -> None:
        self.steps = steps

    def __str__(self) -> str:
        clz_name = self.__class__.__name__
        return f'class name : {clz_name}, ' + ' '.join([str(step) for step in self.steps])

    def handle(self, line: str) -> str:
        for step in self.steps:
            handled = step.handle(line)
            if handled and not handled.isspace():
                return handled
        return ""

    def finish(self):
        for step in self.steps:
            step.finish()