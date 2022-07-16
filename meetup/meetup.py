from datetime import date
import calendar
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    week_matching = {"first": 1, "second": 2, "third": 3, "fourth": 4}
    desired_counter = -1
    if week in week_matching:
        desired_counter = week_matching.get(week)
    elif week == 'teenth':
        pass
    c = calendar.Calendar()
    day_counter = 0
    current_answer = ''
    week_calendar = c.monthdatescalendar(year, month)
    for calendar_week in week_calendar:
        for calendar_day in calendar_week:
            if day_counter == desired_counter:
                return current_answer
            if calendar_day.strftime('%A') == day_of_week and calendar_day.month == month: # FIRST
                day_counter += 1
                current_answer = calendar_day
            
# Look into the datetime module cause it probably gives us everything
# note that teenth will be the only weird Day of Week. 