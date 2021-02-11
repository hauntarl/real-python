import re
from datetime import datetime
from typing import List


# TODO: create a factory method to accept date format as string (refactor acc.)
class DateChecker:
    """
    DateChecker defines a date-time format and verifies whether input string matches
    the specified format
    . setup up a format to compare date values. 
      DateChecker(DateChecker.year, DateChecker.month, DateChecker.day)
    . verify() method - takes in a single string input and matches it against the 
      specified format
    . verify_list() method - takes a list of strings as input
    . to_datetime() method - converts the given string input to a datetime 
      object.
    """
    year = r'(?P<year>\d{4})'  # regex for year: YYYY
    month = r'(?P<month>(?:0[1-9])|(?:1[0-2]))'  # regex for month: MM
    day = r'(?P<day>(?:0[1-9])|(?:[12]\d)|(?:3[01]))'  # regex for day: DD
    hour = r'(?P<hour>(?:2[0-3])|(?:[01]\d))'  # regex for hours: hh
    minute = r'(?P<minute>[0-5]\d)'  # regex for minutes: mm
    second = r'(?P<second>[0-5]\d)'  # regex for seconds: ss
    millisecond = r'(?P<millisecond>\d{3})'  # regex for milliseconds: mil
    microsecond = r'(?P<microsecond>\d{6})'  # regex for microseconds: micros
    # regex for time: hh:mm:ss.mil/micros
    time = fr'(?P<time>\s*{hour}[:]{minute}[:]{second}' \
        fr'[.]({millisecond}|{microsecond}))?'

    def __init__(self, *args: List[str], sep: str = '-') -> None:
        if len(args) != 3:
            raise AttributeError('Positional parameters passed must be 3')

        # regular expression based on user-specific format
        self.sep = f'[{sep}]'  # date separator symbol
        exp = f'^{self.sep.join(args)}{self.time}$'
        self.regex = re.compile(exp)

    def to_datetime(self, inp: str) -> datetime:
        result = self.regex.search(inp)
        if result is None:
            return

        d = result.groupdict()
        YY, MM, DD = int(d['year']), int(d['month']), int(d['day'])
        if d['time'] is None:
            return datetime(YY, MM, DD)

        hh, mm, ss = int(d['hour']), int(d['minute']), int(d['second'])
        mili, micro = d['millisecond'], d['microsecond']
        mili = (int(mili) * 1000) if mili else 0
        micro = int(micro) if micro else 0
        return datetime(YY, MM, DD, hh, mm, ss, mili if mili else micro)

    def verify(self, inp: str) -> bool:
        return True if self.to_datetime(inp) else False

    def verify_list(self, inp_list: List[str]) -> bool:
        for index in range(len(inp_list)):
            if self.verify(inp_list[index]):
                continue
            print(f'Invalid Date \'{inp_list[index]}\' at index: {index}')
            return False

        print('All dates match the specified format')
        return True


dc = DateChecker(DateChecker.year, DateChecker.month, DateChecker.day)
print(dc.regex)
dt = dc.to_datetime('2020-12-31')
print(repr(dt))
dt = dc.to_datetime('2020-12-31 23:59:59.000001')
print(repr(dt))

print(dc.verify('2020-12-31'), '\tformat: YYYY:MM:DD')
print(dc.verify('2020-13-31'), '\tmonth greater than 12')
print(dc.verify('2020-12-32'), '\tday greater than 31')
print(dc.verify('2020-00-31'), '\tmonth cannot be 0')
print(dc.verify('2020-12-00'), '\tday cannot be zero')
print(dc.verify('10000-12-31'), '\tyear greater than 9999')
print()
print(dc.verify('2020-31-12'), '\tformat: YYYY:DD:MM')
print(dc.verify('31-12-2020'), '\tformat: DD:MM:YYYY')
print(dc.verify('12-31-2020'), '\tformat: MM:DD:YYYY')
print()
print(dc.verify('2020-12-31 23:59:59.999'), '\tYYYY:MM:DD hh:mm:ss.mil')
print(dc.verify('2020-13-31 23:59:59.999'), '\tmonth greater than 12')
print(dc.verify('2020-12-32 23:59:59.999'), '\tday greater than 31')
print(dc.verify('2020-00-31 23:59:59.999'), '\tmonth cannot be 0')
print(dc.verify('2020-12-00 23:59:59.999'), '\tday cannot be zero')
print(dc.verify('10000-12-32 23:59:59.999'), '\tyear greater than 9999')
print()
print(dc.verify('2020-31-12 23:59:59.999'), '\tYYYY:DD:MM hh:mm:ss.mil')
print(dc.verify('31-12-2020 23:59:59.999'), '\tDD:MM:YYYY hh:mm:ss.mil')
print(dc.verify('12-31-2020 23:59:59.999'), '\tMM:DD:YYYY hh:mm:ss.mil')
print()
print(dc.verify('2020-12-31 24:59:59.999'), '\thours > 23')
print(dc.verify('2020-12-31 23:60:59.999'), '\tminutes > 59')
print(dc.verify('2020-12-31 23:59:60.999'), '\tseconds > 59')
print(dc.verify('2020-12-31 23:59:59.1000'), '\tmiliseconds > 999')

print()
input_list = ['2020-12-31', '2020-12-31', '2020-12-31', '2020-12-32']
print(input_list)
dc.verify_list(input_list)
