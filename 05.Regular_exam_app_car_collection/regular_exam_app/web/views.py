from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def get_profile():
    profile_set = Profile.objects.all()
    if profile_set:
        return profile_set[0]
    else:
        return None


def show_home(request):
    profile = get_profile()
    context = {
        "profile": profile,
    }
    return render(request, "index.html", context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_cars = len(cars)
    context = {
        "profile": profile,
        "cars": cars,
        "total_cars": total_cars,
    }
    return render(request, "catalogue.html", context)


def car_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()
    context = {
        'form': form,
        "profile": profile,
    }
    return render(request, "car-create.html", context)


def car_details(request, pk):
    profile = Profile.objects.all()
    current_car = Car.objects.get(pk=pk)
    context = {
        "current_car": current_car,
        "profile": profile,
            }
    return render(request, "car-details.html", context)


def car_edit(request, pk):
    profile = get_profile()
    current_car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=current_car)
    context = {
        'form': form,
        "current_car": current_car,
        "profile": profile,
    }
    return render(request, "car-edit.html", context)


def car_delete(request, pk):
    profile = get_profile()
    current_car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=current_car)
    context = {
        'form': form,
        "current_car": current_car,
        "profile": profile,
    }
    return render(request, "car-delete.html", context)


def create_profile(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catalogue')
        else:
            form = CreateProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'profile-create.html', context)
    # book_list = Book.objects.all()
    context = {
        # 'book_list': book_list,
        "profile": profile,
    }
    return render(request, "catalogue.html", context)


def profile_details(request):
    profile = get_profile()

    total_cost = Car.objects.all().aggregate(Sum("price"))

    if profile.profile_picture is None:
        image = False
    else:
        image = True

    if profile.first_name is None:
        first_name = False
    else:
        first_name = True

    if profile.last_name is None:
        last_name = False
    else:
        last_name = True

    context = {
        "profile": profile,
        "image": image,
        "total_cost": total_cost["price__sum"],
        "first_name": first_name,
        "last_name": last_name,

    }
    return render(request, "profile-details.html", context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        "profile": profile,
    }
    return render(request, "profile-edit.html", context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        "profile": profile,
    }
    return render(request, "profile-delete.html", context)


