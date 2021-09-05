from datetime import datetime
from operator import gt, lt
import os
import glob
from pipline import Search, Write, AllStep, AnyStep, Context, Date
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
    # any_steps = [
    #     Search('(?=POST|GET)'),
    # ]
    # anyContext = AnyStep(any_steps)
    final_steps = [
        Search(r'(?=POST|GET)'),
        Write(os.path.join(DEST_LOG_FOLDER, 'post_get.log')),
        Date(DATE_TIME_PATTERN, time=datetime(year=2021, month=9, day=7), cmp=gt),
        # Search('response', block_if_match=True),
        Write(os.path.join(DEST_LOG_FOLDER, 'after_9_7.log'))
    ]
    final = AllStep(final_steps)
    return Context([final])

DATE_TIME_PATTERN = r"(?<=[\[]{1})(?P<day>[\d]{2})[\/]{1}(?P<month>[a-zA-Z]+)[\/]{1}(?P<year>[0-9]+):(?P<hour>[0-9]+):(?P<minute>[0-9]+):(?P<second>[0-9]+) .*(?=[\]])"

if __name__ == '__main__':
    log_paths = [path
                 for path in glob.glob(os.path.join(SRC_LOG_FOLDER, 'fake*.log'))]
    pipline = define_pipline()
    pipline.exec(load_logs(log_paths))