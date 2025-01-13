from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponseForbidden # type: ignore
from .forms import EventForm
from datetime import date
from django.contrib.auth.models import User # type: ignore
from .models import Event


def home(request):
    # Pobranie aktualnej daty
    today = date.today()

    if request.user.is_authenticated:
        # Pobranie wydarzeń dla zalogowanego użytkownika
        user = request.user
        events = Event.objects.filter(user=user).order_by('start_time')
    else:
        user = None
        events = []

    # Renderowanie strony głównej
    return render(request, 'home.html', {
        'today': today,
        'events': events,
        'user': user,
    })

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Przekierowanie po zapisaniu
    else:
        form = EventForm()
    
    return render(request, 'add_event.html', {'form': form})

@login_required
def event_detail(request, event_id):
    # Pobranie wydarzenia lub zwrócenie błędu 404
    event = get_object_or_404(Event, id=event_id)

    if event.user != request.user:
        return HttpResponseForbidden("Nie masz dostępu do tego wydarzenia.")
    
    return render(request, 'event_detail.html', {'event': event})