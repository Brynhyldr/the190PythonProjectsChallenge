import datetime
import math

def age_calculator(year, month, day):
    today = datetime.date.today()
    dob = datetime.date(year, month, day)
    return math.trunc(abs((today - dob).days)/365.25)