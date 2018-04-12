from django.contrib import admin
from .models import Comment, Event, Order
# Register your models here.
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Order)
