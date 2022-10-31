from django.shortcuts import render, redirect
from my_music_app.web.forms import CreateProfileForm
from my_music_app.web.models import Profile
from .forms import *
from .models import *


def get_profile():
    profile_set = Profile.objects.all()
    if profile_set:
        return profile_set[0]
    else:
        return None


def get_albums():
    albums_set = Album.objects.all()
    if albums_set:
        return albums_set
    else:
        return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    album_list = Album.objects.all()
    context = {
        'album_list': album_list,
    }
    return render(request, 'home-with-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, initial={'album_name': 'Album Name', 'artist': 'Artist',
                                                      'description': 'Description', 'image_url': "Image URL",
                                                      "price": "Price",
                                                      })
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateAlbumForm(initial={'album_name': 'Album Name', 'artist': 'Artist',
                                        'description': 'Description', 'image_url': "Image URL",
                                        "price": "Price",
                                        })
    context = {
        'form': form,
        'no_albums': True
    }
    return render(request, 'home-with-profile.html', context)


def album_details(request, pk):
    current_album = Album.objects.get(pk=pk)
    context = {
        "album": current_album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    current_album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=current_album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditAlbumForm(instance=current_album)
    context = {
        'form': form,
        'no_albums': True,
        "album": current_album,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    current_album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=current_album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteAlbumForm(instance=current_album)
    context = {
        'form': form,
        'no_albums': True,
        "album": current_album,
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, initial={"age": 0, 'user_name': 'Username', 'e_mail': 'E-mail'})
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm(initial={"age": 0, 'user_name': 'Username', 'e_mail': 'E-mail'})
    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)

    context = {
        "profile": profile,
        "albums_count": albums_count,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):

    return render(request, 'profile-delete.html')
