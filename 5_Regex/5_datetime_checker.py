import re


# DateChecker defines a date-time format and verifies whether input string
# matches the specified format
# ^\d{4}-(?:(?:0[1-9])|(?:1[0-2]))-(?:(?:0[1-9])|(?:[12]\d)|(?:3[01]))(?:\s*(?:(?:2[0-3])|(?:[01]\d)):[0-5]\d:[0-5]\d.\d{3})?$
# regex to match the format: YYYY-MM-DD hh:mm:ss.mili
class DateChecker:
    # regex for year: YYYY
    year = r'\d{4}'
    # regex for month: MM
    month = r'(?:(?:0[1-9])|(?:1[0-2]))'
    # regex for day: DD
    day = r'(?:(?:0[1-9])|(?:[12]\d)|(?:3[01]))'
    # regex for time: hh:mm:ss.mil
    time = r'(?:\s*(?:(?:2[0-3])|(?:[01]\d)):[0-5]\d:[0-5]\d.\d{3})?'

    def __init__(self, *args, sep='-'):
        self.sep = sep  # date separator symbol

        # positional arguments must be 3 and any possible combination of year,
        # month and day
        if len(args) != 3:
            raise AttributeError(f'required arguments: 3, got:{len(args)}')

        # regular expression based on user-specified format
        exp = f'^{self.sep.join(args)}{self.time}$'
        self.regex = re.compile(exp)

    def verify(self, date):
        return True if self.regex.search(date) else False, date

    def verify_list(self, dates):
        for index in range(len(dates)):
            if self.verify(dates[index]):
                continue
            return False, f'Invalid Date format {dates[index]} at index: {index}'

        return True, 'All dates match the specified format'


dc = DateChecker(DateChecker.year, DateChecker.month, DateChecker.day)
print(dc.verify('2020-12-31'), '\tYYYY:MM:DD')
print(dc.verify('2020-13-31'), '\tmonth greater than 12')
print(dc.verify('2020-12-32'), '\tday greater than 31')
print(dc.verify('2020-00-31'), '\tmonth cannot be 0')
print(dc.verify('2020-12-00'), '\tday cannot be zero')
print(dc.verify('10000-12-31'), '\tyear greater than 9999')
print()
print(dc.verify('2020-31-12'), '\tYYYY:DD:MM')
print(dc.verify('31-12-2020'), '\tDD:MM:YYYY')
print(dc.verify('12-31-2020'), '\tMM:DD:YYYY')  # why does this even exists
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
print(dc.verify('2020-12-31 24:59:59.999'), '\thours greater than 23')
print(dc.verify('2020-12-31 23:60:59.999'), '\tminutes greater than 59')
print(dc.verify('2020-12-31 23:59:60.999'), '\tseconds greater than 59')
print(dc.verify('2020-12-31 23:59:59.1000'), '\tmiliseconds greater than 999')
