from datacenter.models import Visit
from django.shortcuts import render
from datacenter.helpers import format_duration, get_duration


def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in non_leaved_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        time_then = visit.entered_at
        author = visit.passcard

    non_closed_visit = [
        {
            'who_entered': author.owner_name,
            'entered_at': time_then,
            'duration': formatted_duration,
        }
    ]
    non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
