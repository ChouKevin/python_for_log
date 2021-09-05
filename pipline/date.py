import re
import operator
import calendar
from typing import Mapping
from .step import Step
from datetime import datetime


class Date(Step):
    """
    cmp: see `operator` module. using le lt ge gt. 
            cmp(log_time, given_time).

    pattern: named group pattern. 
            it contains name: `year` `month` `day` `hour` `minute` `second` `microsecond` `tzinfo`.
    
    auto_pass: default=True. because of log is sequential message, if it read the log that
            let result of cmp changed, then dont do cmp anymore.
    """
    def __init__(self, pattern: str, time: datetime
                , cmp: operator, auto_pass: bool=True) -> None:
        self.pattern = pattern
        self.time = time
        self.cmp = cmp
        self.auto_pass = auto_pass
        self.need_cmp = True
        self.prev_cmp_result = None
        self.abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
    
    def handle(self, line: str) -> str:
        if self.need_cmp:
            time_info = re.search(self.pattern, line).groupdict()
            self._trans_time_info(time_info)
            log_time = datetime(**time_info)
            cur_cmp_result = self.cmp(log_time, self.time)
            self._trigger_cmp(cur_cmp_result)
            return line if cur_cmp_result else ""
        return line if self.prev_cmp_result else ""
    
    def _trigger_cmp(self, cur_cmp_result: bool):
        if not self.auto_pass: return
        if self.prev_cmp_result is None:
            self.prev_cmp_result = cur_cmp_result
        else:
            if self.prev_cmp_result != cur_cmp_result:
                self.prev_cmp_result = cur_cmp_result
                self.need_cmp = False
    
    def _trans_time_info(self, time_info: Mapping[str, str]) :
        for k, v in time_info.items():
            if k == 'month' and not v.isdigit():
                time_info.update({k: self.abbr_to_num[v]})
            elif k == 'microsecond':
                time_info.update({k: float(v)})
            elif k == 'tzinfo':
                raise NotImplemented
            else:
                time_info.update({k: int(v)})