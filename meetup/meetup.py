from datetime import date
from calendar import monthrange


def meetup_day(year, month, day_of_the_week, which):
    weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
                'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    # first_day_of_month = datetime.date(year, month, 1).weekday()

    # Get the first Monday/Tuesday/etc. of the month.
    first_which = 1
    while date(year, month, first_which).weekday() \
            != weekdays[day_of_the_week] % 7:
        first_which += 1

    if which == 'teenth':
        # Only one "teenth" for each day of the week.
        return date(year, month, get_teenth_which(first_which))
    elif which == 'last':
        return date(year, month, get_last_which(year, month, first_which))
    else:
        try:
            return date(year, month, first_which +
                        ((int(which[0]) - 1) * 7))
        except ValueError:
            raise MeetupDayException(
                'There is no {0} {1} for this month.'
                .format(which, day_of_the_week)) from None


def get_teenth_which(first_which):
    teenth_which = first_which
    while teenth_which < 13:
        teenth_which += 7
    return teenth_which


def get_last_which(year, month, first_which):
    last_which = first_which
    days_in_month = monthrange(year, month)[1]
    # Guard against overshooting the end of the month.
    while last_which < days_in_month - 6:
        last_which += 7
    return last_which


class Error(Exception):
    pass


class MeetupDayException(Error):
    pass
