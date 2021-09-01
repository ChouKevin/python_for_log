import os
from pipline import RegexPipe, WritePipe, Context, AnyContext, PrintPipe
from definitinos import *
from typing import Iterable


def load_line_by_line(path: str) -> Iterable[str]:
    with open(path) as f:
        for line in f.readlines():
            yield line


def load_logs(paths: Iterable[str]) -> Iterable[str]:
    for path in paths:
        for log_info in load_line_by_line(path):
            yield log_info


def define_pipline() -> Context:
    any_steps = [
        RegexPipe('user 131313'),
        RegexPipe('user 131'),
    ]
    anyContext = AnyContext(any_steps)
    final_steps = [
        anyContext,
        WritePipe(os.path.join(DEST_LOG_FOLDER, 'contains_user.log')),
        RegexPipe('response', block_if_match=True),
        WritePipe(os.path.join(DEST_LOG_FOLDER, 'remove_response.log'))
    ]
    return Context(final_steps)


if __name__ == '__main__':
    mass_log_files = ['test.log']
    log_paths = [os.path.join(SRC_LOG_FOLDER, filename)
                 for filename in mass_log_files]
    pipline = define_pipline()
    for log_info in load_logs(log_paths):
        pipline.handle(log_info)
    pipline.finish()