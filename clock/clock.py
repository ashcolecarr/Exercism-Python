class Clock(object):
    _minutes_in_hour = 60
    _minutes_in_day = 1440

    def __init__(self, hour, minute):
        clock_time = (((hour * self._minutes_in_hour) +
                       minute) % self._minutes_in_day)
        self.hour, self.minute = divmod(clock_time, self._minutes_in_hour)

    def __repr__(self):
        return '{0.hour:02d}:{0.minute:02d}'.format(self)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
