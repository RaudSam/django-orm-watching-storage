from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.helpers import format_duration, get_duration, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        long_visit = is_visit_long(duration)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formatted_duration,
                'is_strange': long_visit
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
