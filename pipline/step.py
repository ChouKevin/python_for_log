from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def handle(self, line: str) -> str :
        return NotImplemented

    def finish(self):
        pass