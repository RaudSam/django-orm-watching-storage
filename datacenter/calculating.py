from django.utils.timezone import localtime, now

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
    seconds = duration.seconds
    minutes = (seconds % 3600) // 60
    hours = seconds // 3600
    return f'{hours}ч {minutes}мин'


def is_visit_long(duration, hour=60):
    minutes = (duration.seconds // 60)
    return minutes < hour