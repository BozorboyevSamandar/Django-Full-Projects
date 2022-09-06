from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from base.models import Topic
from .forms import UserForm, MyUserCreationForm


# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            username = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password does not exits")

    context = {'page': page}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'An Error occured during registration')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_message': room_message, 'topics': topics}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def userUpdate(request, pk):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            redirect('user-profile', pk=user.id)
    context = {'form': form}
    return render(request, 'update-user.html', context)
