from django.shortcuts import render, redirect
from .forms import EventForm
from datetime import date
from django.contrib.auth.models import User
from .models import Event


def home(request):
    # Pobranie aktualnej daty
    today = date.today()
    
    # Tymczasowy wybór użytkownika
    user_id = request.GET.get('user')  # Pobieramy ID użytkownika z parametru GET
    if user_id:
        user = User.objects.get(id=user_id)
        events = Event.objects.filter(user=user).order_by('start_time')
    else:
        user = None
        events = []

    # Renderowanie strony głównej
    return render(request, 'home.html', {
        'today': today,
        'events': events,
        'users': User.objects.all(),  # Lista użytkowników do wyboru
        'selected_user': user
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

