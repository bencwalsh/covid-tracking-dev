class DateRequest:
    def __init__(self, date='20200501'):
        self._date = date

    @property
    def date(self):
        return self._date
