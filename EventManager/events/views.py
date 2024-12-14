from django.shortcuts import render
from django.http import HttpResponse

# Hardcoded data for events
upcoming_events = [
    {"title": "Tech Conference", "date": "2024-12-20", "description": "A conference about the latest in tech."},
    {"title": "Music Festival", "date": "2025-01-15", "description": "A festival with live music from various artists."}
]

past_events = [
    {"title": "Cooking Workshop", "date": "2024-06-15", "feedback": "Great experience! Everyone loved the cooking tips."},
    {"title": "Art Exhibition", "date": "2024-08-01", "feedback": "The exhibition showcased amazing pieces of art."}
]

def homepage(request):
    return render(request, 'home.html')

def upcoming_events_view(request):
    return render(request, 'upcoming_events.html', {'events': upcoming_events})

def past_events_view(request):
    return render(request, 'past_events.html', {'events': past_events})

def event_details_view(request, event_id):
    try:
        event = upcoming_events[event_id]  # Using the event_id to fetch data
    except IndexError:
        return HttpResponse("Event not found.", status=404)
    return render(request, 'event_details.html', {'event': event})

def contact_view(request):
    return render(request, 'contact.html')
