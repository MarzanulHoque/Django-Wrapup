from django.shortcuts import render
from .models import Destination


def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'City never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Hayderabad'
    dest2.desc = 'Pehle biriany ,fir sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Chennai'
    dest3.desc = 'Good city for Tech'
    dest3.img = 'destination_3.jpg'
    dest3.price = 900

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
