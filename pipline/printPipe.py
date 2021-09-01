from .step import Step

class PrintPipe(Step):
    def __init__(self) -> None:
        pass
    
    def handle(self, line: str) -> str:
        print(line)
        return line