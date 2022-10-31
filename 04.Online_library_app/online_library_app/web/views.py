from django.shortcuts import render, redirect

from online_library_app.web.forms import *
from online_library_app.web.models import Profile, Book


def get_profile():
    profile_set = Profile.objects.all()
    if profile_set:
        return profile_set[0]
    else:
        return None


def home_page(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = CreateProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
        "profile": profile,
    }
    return render(request, "home-with-profile.html", context)


def book_add(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateBookForm()
    context = {
        'form': form,
    }
    return render(request, "add-book.html", context)


def book_edit(request, pk):
    current_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=current_book)
    context = {
        'form': form,
        "current_book": current_book,
    }
    return render(request, "edit-book.html", context)


def book_details(request, pk):
    current_book = Book.objects.get(pk=pk)
    context = {
        "current_book": current_book,
        "no_profile": True,
            }
    return render(request, "book-details.html", context)


def book_delete(request, pk):
    Book.objects.filter(id=pk).delete()
    return redirect("home page")


def profile_page(request):
    profile = get_profile()
    if profile.profile_image_url is None:
        image = False
    else:
        image = True
    context = {
        "profile": profile,
        "image": image,
    }
    return render(request, "profile.html", context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        "profile": profile,
    }
    return render(request, "edit-profile.html", context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context,)
