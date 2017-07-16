from datetime import datetime


def current_time(*args):
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M")


KEYWORDS = {
    ("time", "date", "day"): current_time
}