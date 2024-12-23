from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passanger
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, "flights/flights.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passangers": flight.passangers.all(),
        "non_passangers": Passanger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passanger = Passanger.objects.get(pk=int(request.POST["passanger"]))
        passanger.flights.add(flight)
        # return HttpResponseRedirect(reverse("index")) 

def user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "flights/user.html", {
                "form": form
            })
    else:
        form = UserForm()
    return render(request, "flights/forms.html", {
        "form": form
    })