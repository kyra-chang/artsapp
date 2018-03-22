from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import CommentForm

from django.http import HttpResponse
from django.template import loader

from .models import Event

from .models import Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, OrderForm
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import Profile, Event
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

# - Kyra 3.19.2018
# this method is to render index
def index(request):
    return render(request, 'alpha/index.html', {})

# - Kyra 3.19.2018
# this method is for testing the homepage feature (lists of events), not really finished
def home(request):
    events = Event.objects.all()
    return render(request, 'form/home.html', { 'events': events })

# - Kyra 3.22.2018
# UNDER CONSTRUCTION
# this method is to checkin
# def event_checkin(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.event = event
#             comment.created_date = timezone.now()
#             comment.save()
#     else:
#         form = CommentForm()
#     return render(request, 'form/event.html', {
#         'form': form, 'event': event
#     })

# - Kyra 3.22.2018
# this method is to order the tickets
def event_order(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.event = event
            order.order_date = timezone.now()
            order.save()
            messages.success(request, 'You ordered the tickets!')
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
    else:
        form = CommentForm()
    return render(request, 'form/event.html', {
        'form': form, 'event': event
    })

# - Kyra 3.19.2018
# this method is for creating the user and its related profile after submitting the form
@transaction.atomic
def profile_create(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save() # Gracefully save the form
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'user/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# - Kyra 3.19.2018
# this class is for updating the profile after submitting the form
# so we actually have 2 ways to write the controller
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "user/profile_update.html"
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.profile

    def get_success_url(self, *args, **kwargs):
        return reverse("user")

# - Kyra 3.19.2018
# This method is just render the related html file for viewing the user dashboard
def UserView(request):
    return render(request, 'user/user.html', {
    })
	
# Done by Alex
# Displays the five latest events (shows a picture of the events and you can click on them to get to the event page)
def index(request):
    latest_event_list = Events.objects.order_by('-event_date')[:5]
    template = loader.get_template('aC_bookfest/index.html')
    context = {
        'latest_event_list': latest_event_list,
    }
    return HttpResponse(template.render(context, request))


