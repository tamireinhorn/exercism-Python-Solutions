from datetime import date, datetime
import calendar
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def _check_calendar_day(calendar_day: date, day_of_week: str, month: int):
    return calendar_day.strftime('%A') == day_of_week and calendar_day.month == month


def _ordinal_meetup(week_calendar: list[list[date]], day_of_week: str, month: int, desired_counter: int):
    day_counter = 0
    for calendar_week in week_calendar:
        for calendar_day in calendar_week:
            if day_counter == desired_counter:
                return current_answer
            if _check_calendar_day(calendar_day, day_of_week, month): # FIRST
                day_counter += 1
                current_answer = calendar_day
    raise MeetupDayException("That day does not exist.")


def _teenth(week_calendar: list[list[date]], day_of_week: str, month: int):
    for calendar_week in week_calendar:
            for calendar_day in calendar_week:
                if calendar_day.day >= 13 and _check_calendar_day(calendar_day, day_of_week, month):
                    return calendar_day


def _last(week_calendar: list[list[date]], day_of_week: str, month: int):
    for calendar_week in week_calendar[::-1]:
        for calendar_day in calendar_week:
            if _check_calendar_day(calendar_day, day_of_week, month):
                return calendar_day


def meetup(year: int, month: int, week: str, day_of_week: str):
    c = calendar.Calendar()
    week_matching = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
    week_calendar = c.monthdatescalendar(year, month)
    if week in week_matching:
        return _ordinal_meetup(week_calendar, day_of_week, month, week_matching.get(week))
    elif week == 'teenth':
        return _teenth(week_calendar, day_of_week, month)
    elif week == 'last':
        return _last(week_calendar, day_of_week, month)
