from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Event(models.Model):  
    name = models.CharField(max_length=500)
    time = models.DateField()
    organizer = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    points = models.IntegerField()

class Order(models.Model):  
    event = models.ForeignKey("Event", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey("User", null=False, db_column="studentId")
    order_date = models.Datefield(null=False)
    order_checkin = models.IntegerField()

class Interested(models.Model): 
    user = models.ForeignKey("User", null=False, db_column="studentId")
    event = models.ForeignKey("Event", null=False, db_column="eventId")
    
class Comment(models.Model):    
    event = models.ForeignKey("Event", null=False, db_column="eventId")
    user = models.ForeignKey("User", null=False, db_column="studentId")
    comment = models.TextField()
    photo = models.FileField(upload_to='documents/')
    created_date = models.DateTimeField(default=timezone.now)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class EventInfo(models.Model):
    Title = models.CharField(max_length=255, blank=True)
    Location = models.CharField(max_length=255, blank=True)
    Time = models.DateTimeField(auto_now_add=True)
    Description = models.CharField(max_length=10000, blank=True)
    Cost = models.IntegerField(max_length=500)
#for the use of the extending User model, please go to this website:
#https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#extending-the-existing-user-model
#Sign Up With Profile Model
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
#https://gist.github.com/vitorfs/cbe877156ba538a20c53c9a1cea29277
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,
        related_name='profile',
    )
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRAD = 'GR'
    YEAR_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRAD, 'Graduate')
    )
    M = 'M'
    F = 'F'
    O = 'O'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
        (O, 'Other')
    )
    year = models.CharField(
        max_length=2, blank=True,
        choices=YEAR_CHOICES,null=True,
    )
    major = models.CharField(max_length=50,null=True,blank=True,)
    age = models.IntegerField(null=True,blank=True,)
    gender = models.CharField(
        max_length=1,null=True,blank=True,
        choices=GENDER_CHOICES,
    )
    points = models.IntegerField(null=True,blank=True,)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
