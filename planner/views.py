from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.contrib import messages
from .models import Location, PicnicSpot, WeatherSubscription

# Create your views here.

def fetch_weather_data(latitude, longitude):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def index(request):
    try:
        locations = Location.objects.all()
    except Exception as e:
        print(f"Error fetching locations: {e}")
        messages.error(request, "There was an error fetching locations.")
        locations = []
    return render(request, 'index.html', {'locations': locations})

def picnic_spots(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    weather_data = fetch_weather_data(location.latitude, location.longitude)
    if weather_data is None:
        messages.error(request, "Could not fetch weather data at this time.")
    try:
        picnic_spots = PicnicSpot.objects.filter(location=location).order_by('distance')
    except Exception as e:
        print(f"Error fetching picnic spots: {e}")
        messages.error(request, "There was an error fetching picnic spots.")
        picnic_spots = []
    return render(request, 'picnic_spots.html', {'location': location, 'weather_data': weather_data, 'picnic_spots': picnic_spots})

def subscribe(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == "POST":
        email = request.POST.get('email')
        time_slot = request.POST.get('time_slot')
        if not email or not time_slot:
            messages.error(request, "Email and time slot are required.")
            return redirect('subscribe', location_id=location_id)
        try:
            subscription = WeatherSubscription(email=email, location=location, time_slot=time_slot)
            subscription.save()
            messages.success(request, "Subscription successful.")
            return render(request, 'subscribe_success.html', {'subscription': subscription})
        except Exception as e:
            print(f"Error saving subscription: {e}")
            messages.error(request, "There was an error saving your subscription.")
            return redirect('subscribe', location_id=location_id)
    else:
        return render(request, 'subscribe.html', {'location': location})
