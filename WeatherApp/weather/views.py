import requests
from django.shortcuts import render

from weather.models import City
from .forms import CityForm

def index(request):
    appid = 'b300335257bd27af77b0aa5b65c38a3b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon']

            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form':  form}

    return render(request, 'weather/index.html', context)


