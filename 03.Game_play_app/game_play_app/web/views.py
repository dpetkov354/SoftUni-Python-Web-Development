from django.db.models import Avg
from django.shortcuts import render, redirect

from game_play_app.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from game_play_app.web.models import Profile, Game


def get_profile():
    profile_set = Profile.objects.all()
    if profile_set:
        return profile_set[0]
    else:
        return None


def home_page(request):
    profile = get_profile()
    if profile is not None:
        context = {
            "no_profile": True,
        }
    else:
        context = {
            "no_profile": False,
        }
    return render(request, "home-page.html", context)


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateGameForm()
    context = {
        'form': form,
        "no_profile": True,
    }
    return render(request, "game/create-game.html", context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        "no_profile": True,
        "games": games,
    }
    return render(request, "game/dashboard.html", context)


def details_game(request, pk):
    current_game = Game.objects.get(pk=pk)
    context = {
        "current_game": current_game,
        "no_profile": True,
            }
    return render(request, "game/details-game.html", context)


def edit_game(request, pk):
    current_game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=current_game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=current_game)
    context = {
        'form': form,
        "no_profile": True,
        "current_game": current_game,
    }
    return render(request, "game/edit-game.html", context)


def delete_game(request, pk):
    current_game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=current_game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=current_game)
    context = {
        'form': form,
        "no_profile": True,
        "current_game": current_game,
    }
    return render(request, "game/delete-game.html", context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    else:
        form = CreateProfileForm()
    context = {
        "form": form,
    }
    return render(request, "profile/create-profile.html", context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    game_count = len(games)
    avg_rating = Game.objects.aggregate(Avg('rating'))
    if profile.image_url is None:
        image = False
    else:
        image = True
    context = {
        "profile": profile,
        "game_count": game_count,
        "avg_rating": avg_rating["rating__avg"],
        "no_profile": True,
        "image": image,
    }
    return render(request, "profile/details-profile.html", context)


def delete_profile(request):
    profile = Profile.objects.all()
    Game.objects.all().delete()
    profile.delete()
    return redirect('home page')


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        "no_profile": True,
        "profile": profile,
    }
    return render(request, "profile/edit-profile.html", context)


