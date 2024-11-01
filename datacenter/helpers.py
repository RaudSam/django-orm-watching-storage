from django.utils.timezone import localtime, now


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


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
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds - hours * SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f'{hours}ч {minutes}мин'


def is_visit_long(duration):
    seconds = duration.total_seconds()

    total_minutes = seconds/SECONDS_IN_MINUTE

    long_visit_minutes = 60
    is_visit_long = total_minutes > long_visit_minutes
    return is_visit_long
