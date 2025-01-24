from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponseForbidden # type: ignore
from django.contrib import messages # type: ignore
from .forms import RegistrationForm
from .forms import EventForm
from datetime import date
from .models import Event


def home(request):
    today = date.today()

    if request.user.is_authenticated:
        user = request.user
        events = Event.objects.filter(user=user).order_by('start_time')
    else:
        user = None
        events = []

    return render(request, 'home.html', {
        'today': today,
        'events': events,
        'user': user,
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało utworzone. Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('/')
    else:
        form = EventForm()
    
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.user != request.user:
        return HttpResponseForbidden("Nie masz dostępu do tego wydarzenia.")
    
    return render(request, 'event_detail.html', {'event': event})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.user != request.user:
        return HttpResponseForbidden("Nie masz dostępu do tego wydarzenia.")

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.user != request.user:
        return HttpResponseForbidden("Nie masz dostępu do tego wydarzenia.")

    if request.method == 'POST':
        event.delete()
        return redirect('home')

    return render(request, 'delete_event.html', {'event': event})