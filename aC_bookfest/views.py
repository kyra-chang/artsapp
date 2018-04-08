from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import CommentForm

from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Event

from .models import Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, OrderForm, DummyForm
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import Profile, Event
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone



def claim(request):
    if request.user.is_authenticated:
        return render(request, 'frontend/claim_tickets.html', {})
    else:
        return redirect("cas_ng_login")


def about(request):
    if request.user.is_authenticated:
        return render(request, 'frontend/about.html', {})
    else:
        return redirect("cas_ng_login")

# - Kyra 3.19.2018
# this method is to render index
def index(request):
    return render(request, 'alpha/index.html', {})

# # - Kyra 3.19.2018
# # this method is to render index
# def testhome(request):
#     return render(request, 'form/home.html', {})

# Done by Alex
# Displays the five latest events (shows a picture of the events and you can click on them to get to the event page)
def home(request):
    latest_event_list = Event.objects.filter(Type='event').order_by('Time')[:5]
    return render(request, 'frontend/index.html', { 'latest_event_list': latest_event_list })

def free(request):
    free_list = Event.objects.filter(Type='free')
    return render(request, 'frontend/free.html', { 'free_list': free_list })


# - Kyra 3.22.2018
# this method is to favorite
# https://stackoverflow.com/questions/5674968/django-query-to-get-users-favorite-posts
def event_favorite(request, pk):

    if request.is_ajax() == True:
        event = get_object_or_404(Event, pk=pk)
        fav = request.user.Profile.favorites
        if event not in fav.all():
            fav.add(event)
            request.user.Profile.save()
        else:
            fav.remove(event)
            request.user.Profile.save()
        # else:
        #     form = DummyForm()
        return HttpResponse(status=200)

# - Kyra 3.22.2018
# UNDER CONSTRUCTION
# this method is to checkin
def event_checkin(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            event = get_object_or_404(Event, pk=pk)
            order = request.user.Profile.orders.filter(Title=event.Title)[0]
            order.order_checkin = timezone.now()
            order.save()
            # TODO verify if the save is success or not
            messages.success(request, 'You checkin!')
            #request.user.Profile.points += 500
            #request.user.Profile.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'form/checkin.html', {
        'form': form
    })

# - Kyra 3.22.2018
# this method is to order the tickets
def event_order(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.Profile = request.user.Profile
            order.event = event
            order.order_date = timezone.now()
            order.save()
            event.Max_order -= 1
            event.save()
            # TODO verify if the save is success or not
            messages.success(request, 'You ordered the tickets!')
            # leave point system and ranking feature later
            #request.user.Profile.points -= event.Cost
            #request.user.Profile.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'form/order.html', {
        'form': form, 'event': event
    })


# - Kyra 3.19.2018
# this method is to upload the pictures and comments for specific events
def event_comment_create(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.event = event
            comment.created_date = timezone.now()
            comment.save()
            # TODO verify if the save is success or not
    else:
        form = CommentForm()
    # return render(request, 'form/event.html', {
    #     'form': form, 'event': event
    # })
    return render(request, 'frontend/event.html', {
        'form': form, 'event': event
    })

# - Kyra 3.19.2018
# this method is for creating the user and its related Profile after submitting the form
"""
@transaction.atomic
def profile_create(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        Profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and Profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            Profile_form = ProfileForm(request.POST, instance=user.Profile)  # Reload the Profile form with the Profile instance
            Profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            Profile_form.save() # Gracefully save the form
            # TODO verify if the save is success or not
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            messages.success(request, 'Your Profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserCreationForm()
        Profile_form = ProfileForm()
    return render(request, 'user/signup.html', {
        'user_form': user_form,
        'Profile_form': Profile_form
    })
"""

# - Kyra 3.19.2018
# this class is for updating the Profile after submitting the form
# so we actually have 2 ways to write the controller
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "user/Profile_update.html"
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.Profile

    def get_success_url(self, *args, **kwargs):
        return reverse("user")

# - Kyra 3.19.2018
# This method is just render the related html file for viewing the user dashboard
def user(request):
    events = request.user.Profile.favorites.all().union(request.user.Profile.orders.all())
    return render(request, 'frontend/myevents.html', { 'events': events
    })
	
# MERGED to index by Kyra
# Done by Alex
# Displays the five latest events (shows a picture of the events and you can click on them to get to the event page)
# def index_back(request):
#     latest_event_list = Event.objects.order_by('Time')[:5]
#     template = loader.get_template('homepage/index.html')
#     context = {
#         'latest_event_list': latest_event_list,
#     }
#     return HttpResponse(template.render(context, request))

# Done by Alex
# Displays top 10 artsiest bears
def TopUsers(request):
    user_list = Profile.objects.order_by('-points')[:10]    
    context_dict = {"users": user_list}
    return render(request, 'ranking/ranking.html', context_dict)

