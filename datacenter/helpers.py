from django.utils.timezone import localtime, now


seconds_in_hour = 3600
seconds_in_minute = 60


def get_duration(visit):
    entered_at = localtime(value=visit.entered_at)
    leaved_at = localtime(value=visit.leaved_at)
    if leaved_at:
        delta = leaved_at - entered_at
    else:
        time_now = localtime(now())
        delta = time_now - entered_at
    return delta


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // seconds_in_hour
    minutes = (total_seconds - hours * seconds_in_hour) // seconds_in_minute
    return f'{hours}ч {minutes}мин'


def is_visit_long(duration):
    seconds = duration.total_seconds()

    total_minutes = seconds/seconds_in_minute

    long_visit_minutes = 60
    is_visit_long = total_minutes > long_visit_minutes
    return is_visit_long
