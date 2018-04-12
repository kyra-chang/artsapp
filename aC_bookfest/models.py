from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def event_pic_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/event_<id>/<filename>
    return 'event_{0}/{1}'.format(instance.id, filename)


class Event(models.Model):
    Title = models.CharField(max_length=255, blank=True)
    s_Title = models.CharField(max_length=255, blank=True,null=True)
    Type = models.CharField(max_length=100, blank=True)
    # either "event" or "free" admission for berkeley students
    Website = models.CharField(max_length=255, blank=True)
    #Organizer = models.CharField(max_length=100)
    Location = models.CharField(max_length=255, blank=True)
    s_Location = models.CharField(max_length=255, blank=True,null=True)
    Time = models.CharField(max_length=100, blank=True)
    s_Time = models.CharField(max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True)
    #Cost = models.IntegerField()
    OfferType = models.CharField(max_length=100, blank=True)
    s_OfferType = models.CharField(max_length=100, blank=True,null=True)
    Max_order = models.IntegerField(null=True,blank=True)
    orders = models.ManyToManyField('Profile', through='Order')
    Picture = models.FileField(upload_to=event_pic_path,null=True,default='settings.MEDIA_ROOT/default.jpg', blank=True)


#for the use of the extending User model, please go to this website:
#https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#extending-the-existing-user-model
#Sign Up With Profile Model
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
#https://gist.github.com/vitorfs/cbe877156ba538a20c53c9a1cea29277
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,
        related_name='Profile',
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
    # M = 'M'
    # F = 'F'
    # O = 'O'
    # GENDER_CHOICES = (
    #     (M, 'Male'),
    #     (F, 'Female'),
    #     (O, 'Other')
    # )
    year = models.CharField(
        max_length=2, blank=True,
        choices=YEAR_CHOICES,null=True,
    )
    major = models.CharField(max_length=50,null=True,blank=True,)
    age = models.IntegerField(null=True,blank=True,)
    # gender = models.CharField(
    #     max_length=1,null=True,blank=True,
    #     choices=GENDER_CHOICES,
    # )
    # TODO set initial value = 0? or 100?
    points = models.IntegerField(null=True,blank=True,default=0)
    favorites = models.ManyToManyField(Event, related_name='favorited_by')
    


# Kyra 3.24
# many-to-many through this intermediate model
# doc: https://docs.djangoproject.com/en/2.0/topics/db/models/#many-to-many-relationships
# create orders model instance, the data will connect between Profile and event in some way
class Order(models.Model):  
    event = models.ForeignKey(Event, null=False, db_column="eventId",on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null=False, related_name='orders', db_column="studentId", on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=False)
    order_confirm = models.BooleanField(default=False)
    order_checkin = models.DateTimeField(null=True)

# Kyra 3.24
# this class is currently not used
class Interested(models.Model): 
    user = models.ForeignKey(User, null=False, db_column="studentId", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, db_column="eventId", on_delete=models.CASCADE)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/event_<id>/<filename>
    return 'event_{0}/comments/{1}'.format(instance.event.id, filename)

class Comment(models.Model):    
    event = models.ForeignKey(Event, related_name='comments', null=False, db_column="eventId", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, db_column="studentId", on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, blank=True)
    photo = models.FileField(upload_to=user_directory_path)
    created_date = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)





@receiver(post_save, sender=User)
def create_user_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Profile(sender, instance, **kwargs):
    instance.Profile.save()
