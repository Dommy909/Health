from django.shortcuts import render, redirect
from .forms import AppointmentForm


def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = AppointmentForm()
    return render(request, 'main/index.html', {'form': form})
