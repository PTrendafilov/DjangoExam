from django.forms import ValidationError
from django.shortcuts import redirect, render
from games.models import *
from games.forms import * 
from django.contrib import messages
# Create your views here.
def home_page(request):
    profile = Profile.objects.first()

    #print("Hello")
    return render(request, 'home-page.html', {'profile':profile})

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        else:
            raise ValidationError('Invalid Data')
    form = CreateProfileForm()
    context = {'form':form}
    return render(request, 'create-profile.html', context)

def details_profile(request):
    profile = Profile.objects.first()
    average_rating = 0
    br=0
    games = Game.objects.all()
    for game in games:
        average_rating+=game.rating
        br+=1
    if br==0:
        average_rating=0
    else:
        average_rating = average_rating/br
    return render(request, 'details-profile.html', {'profile':profile, 'total_games':br, 'average_rating':average_rating})

def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        print(profile)
        context = {'form': EditProfileForm(initial=profile.__dict__), 'profile':profile}
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        print(profile)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('details-profile')
            else:
                context = {'form': form, 'profile':profile}
                return render(request, 'edit-profile.html', context)

def delete_profile(request):
    
    profile = Profile.objects.first()
    games = Game.objects.all()
    if games!='NoneType':
        for game in games:
            game.delete()
    profile.delete()
    return redirect('home-page')

def dashboard(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    return render(request, 'dashboard.html', {'profile':profile, 'games':games})

def game_create(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            raise ValidationError('Invalid Data')
    form = CreateGameForm()
    context = {'form':form, 'profile':profile}
    return render(request, 'create-game.html', context)

def game_details(request ,id):
    profile = Profile.objects.first()
    print(id)
    game=Game.objects.get(id=id)
    return render(request, 'details-game.html', {'game':game, 'profile':profile})

def game_edit(request, id):
    profile = Profile.objects.first()
    game=Game.objects.get(id=id)
    if request.method == "GET":
        context = {'form': CreateGameForm(initial=game.__dict__), 'profile':profile}
        return render(request, 'edit-game.html', context)
    else:
        form = CreateGameForm(request.POST, instance=game)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                context = {'form': form, 'profile':profile}
                return render(request, 'edit-game.html', context)

def game_delete(request,id):
    profile = Profile.objects.first()
    game=Game.objects.get(id=id)
    if request.method == "GET":
        context = {'form': CreateGameForm(initial=game.__dict__), 'profile':profile}
        return render(request, 'delete-game.html', context)
    else:
        if request.method == 'POST':
            Game.objects.get(id=id).delete()
            return redirect('dashboard')