from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Ride, Booking
from .forms import RideForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    rides = Ride.objects.all()

    booked_rides = []
    if request.user.is_authenticated:
        booked_rides = Booking.objects.filter(
            user=request.user
        ).values_list('ride_id', flat=True)

    return render(request, 'home.html', {
        'rides': rides,
        'booked_rides': booked_rides
    })


@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user
            ride.save()
            return redirect('home')
    else:
        form = RideForm()

    return render(request, 'create_ride.html', {'form': form})


@login_required
def book_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)

    # Check if user already booked
    if Booking.objects.filter(ride=ride, user=request.user).exists():
        return redirect('home')

    if ride.seats_available > 0:
        Booking.objects.create(
            ride=ride,
            user=request.user
        )
        ride.seats_available -= 1
        ride.save()

    return redirect('home')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, "my_bookings.html", {
        "bookings": bookings
    })

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.ride.seats_available += 1
        booking.ride.save()
        booking.delete()
    return redirect('my_bookings')

@login_required
def delete_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id, driver=request.user)
    if request.method == 'POST':
        ride.delete()
    return redirect('home')

def home(request):
    rides = Ride.objects.all()
    
    source = request.GET.get('source', '').strip()
    destination = request.GET.get('destination', '').strip()
    date = request.GET.get('date', '').strip()

    if source:
        rides = rides.filter(source__icontains=source)
    if destination:
        rides = rides.filter(destination__icontains=destination)
    if date:
        rides = rides.filter(date=date)

    booked_rides = []
    if request.user.is_authenticated:
        booked_rides = Booking.objects.filter(
            user=request.user
        ).values_list('ride_id', flat=True)

    return render(request, 'home.html', {
        'rides': rides,
        'booked_rides': booked_rides,
        'source': source,
        'destination': destination,
        'date': date,
    })