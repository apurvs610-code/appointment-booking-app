from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def main(request):
    return render(request, 'main.html')

def index(request):
    return render(request, 'index.html')

def book_appointment(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        appointment = form.save()
        return render(request, "success.html", {"data": appointment})
    return render(request, "bookAppointment.html", {"form": form})

def dashboard(request):
    appointments = Appointment.objects.all().order_by('-date')
    return render(request, 'dashboard.html', {'appointments': appointments})

def doctor(request):
    return render(request, 'doctor.html')

def contact(request):
    return render(request, 'contact.html')
