from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.calculating import format_duration, get_duration, is_visit_long

def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at=None)

    for visit in non_leaved_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        time_then = visit.entered_at
        author = visit.passcard

    non_closed_visits = [
        {
            'who_entered': author.owner_name,
            'entered_at': time_then,
            'duration': formatted_duration,
        }
    ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
