from datetime import datetime


def current_time(*args):
    now = datetime.now()
    return now.strftime("%H:%M")


def current_date(*args):
    now = datetime.now()
    return now.strftime("%d-%m-%Y")


KEYWORDS = {
    "time": current_time,
    "date": current_date
}