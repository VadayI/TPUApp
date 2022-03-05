
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.postgres.fields import ArrayField
from django import forms

from django.utils.html import mark_safe


MANAGER_GROUP_NAME = 'Manager'
ADMINISTRATOR_GROUP_NAME = 'Administrator'
APARTMENT_GROUP_NAME = 'Mieszkania'
TRANSPORT_GROUP_NAME = 'Transport'
COLLECTION_GROUP_NAME = 'Collection'
SPONSOR_GROUP_NAME = 'Sponsor'
MEDIA_GROUP_NAME = 'Media'
SUBGROUP_GROUP_NAME = 'Subgroup'
ATTACHMENT_GROUP_NAME = 'Attachment'

APARTMENT_GROUP_TYPE = 1001
TRANSPORT_GROUP_TYPE = 1002
COLLECTION_GROUP_TYPE = 1003
SPONSOR_GROUP_TYPE = 1004
MEDIA_GROUP_TYPE = 1005
ONEOFFACCTION_GROUP_TYPE = 1006
APPLICATION_GROUP_TYPE = 1007
TASK_GROUP_TYPE = 1008

SUBGROUP_GROUP_TYPE = 2001
STATUS_GROUP_TYPE = 2002
ATTACHMENT_GROUP_TYPE= 2003
ADMINISTRATOR_GROUP_TYPE= 2004
MANAGER_GROUP_TYPE= 2005
VOIVODESHIP_GROUP_TYPE = 2006
REGION_GROUP_TYPE = 2007


class Department(Group):
    object_type = IntegerField(unique=True)
    description = TextField(max_length=2000, default='', blank=True)

class Region(models.Model):
    object_type = IntegerField(default=REGION_GROUP_TYPE)
    name = CharField(unique=True, max_length=150, blank=False)
    code = IntegerField(unique=True, blank=False)
    def __str__(self):
        return self.name


class Status(models.Model):
    object_type = IntegerField(default=STATUS_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, unique=True)

    def __str__(self):
        return self.name

class Voivodeship(models.Model):
    object_type = IntegerField(default=VOIVODESHIP_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, unique=True)
    region = ForeignKey(Region, on_delete=CASCADE)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    username = CharField(max_length=150, blank=False, null=False, unique=True)
    city = CharField(max_length=150, blank=True, null=True)
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=True, null=True)
    phone = CharField(max_length=20, blank=True, null=True)
    description = TextField(max_length=2000, default='', blank=True)
    image = models.ImageField(upload_to='attachments/User/image/', null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))

class Attachment(models.Model):
    object_type = IntegerField(default=ATTACHMENT_GROUP_TYPE)
    object_id = IntegerField(blank=False, null=False)
    object_type = IntegerField(blank=False, null=False)
    name = CharField(max_length=150, blank=False)
    file_object = models.FileField(upload_to='attachments/object_type_{}/object_id_{}/%Y_%m_%d'.format(object_type, object_id))
    created_date = DateTimeField(auto_now_add=True)

class Subgroup(models.Model):
    object_type = IntegerField(default=SUBGROUP_GROUP_TYPE)
    name = CharField(max_length=150, blank=True, null=True)
    description = TextField(max_length=2000, default='', blank=True)
    department = models.ForeignKey(Department, on_delete=CASCADE, related_name='subgroups')

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = CharField(max_length=150, blank=False)
    another_name = CharField(max_length=150, blank=True, null=True)
    phone = CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    city = CharField(max_length=150, blank=False)
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=False)
    created_date = DateTimeField(auto_now_add=True)
    modificate_date = DateTimeField(auto_now=True)
    description = TextField(max_length=2000, default='', blank=True)
    archives = BooleanField(default=False)
    subgroup = ForeignKey(Subgroup, on_delete=CASCADE, related_name='objects', blank=True, null=True)

    def __str__(self):
        return self.name

class Apartment(Volunteer):
    object_type = IntegerField(default=APARTMENT_GROUP_TYPE)
    max_number_of_people = IntegerField(default=0)
    current_number_of_people = IntegerField(default=0)
    free_space = IntegerField(default=0)
    operating_range = IntegerField(default=0)
    provides_transportation = BooleanField(default=False)
    available = BooleanField(default=True)
    attachment_1 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True)
    

class Transport(Volunteer):
    object_type = IntegerField(default=TRANSPORT_GROUP_TYPE)
    max_number_of_people = IntegerField(default=0)
    operating_range = IntegerField(default=0)
    available = BooleanField(default=True)
    attachment_1 = models.FileField(upload_to='attachments/Transport/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Transport/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Transport/{}'.format(id), null=True, blank=True)

class Collection(Volunteer):
    object_type = IntegerField(default=COLLECTION_GROUP_TYPE)
    attachment_1 = models.FileField(upload_to='attachments/Collection/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Collection/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Collection/{}'.format(id), null=True, blank=True)

class Sponsor(Volunteer):
    object_type = IntegerField(default=SPONSOR_GROUP_TYPE)
    attachment_1 = models.FileField(upload_to='attachments/Sponsor/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Sponsor/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Sponsor/{}'.format(id), null=True, blank=True)

class Media(Volunteer):
    object_type = IntegerField(default=MEDIA_GROUP_TYPE)
    attachment_1 = models.FileField(upload_to='attachments/Media/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Media/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Media/{}'.format(id), null=True, blank=True)


class OneOffAction(models.Model):
    object_type = IntegerField(default=ONEOFFACCTION_GROUP_TYPE)
    name = CharField(max_length=150, blank=False)
    department = models.ForeignKey(Group, on_delete=PROTECT)
    date_start = DateTimeField(auto_now_add=True)
    date_end = DateTimeField(auto_now_add=True)
    city = CharField(max_length=150, blank=False)
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=False)
    description = TextField(max_length=2000, default='', blank=True)
    status = ForeignKey(Status, on_delete=PROTECT, default=1)
    max_number_of_people = IntegerField()
    current_number_of_people = IntegerField()
    attachment_1 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True)

    
    def __str__(self):
        return self.name

class Application(models.Model):
    object_type = IntegerField(default=APPLICATION_GROUP_TYPE)
    name = CharField(max_length=150, blank=False)
    phone = CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=PROTECT)
    subgroup = ForeignKey(Subgroup, on_delete=CASCADE, related_name='application_objects', blank=True, null=True)
    volunteer = ForeignKey(Volunteer, on_delete=CASCADE, blank=True, null=True)
    created_date = DateTimeField(auto_now_add=True)
    contactApp = CharField(max_length=200, blank=True, null=True)
    status = ForeignKey(Status, on_delete=PROTECT, default=1)
    residence_city = CharField(max_length=150, blank=True, null=True)
    residence_voivodeship = ForeignKey(Voivodeship, related_name='related_app_res_voivodeship', on_delete=PROTECT, blank=True, null=True)
    destination_city = CharField(max_length=150, blank=True, null=True)
    destination_voivodeship = ForeignKey(Voivodeship, related_name='related_app_dest_voivodeship', on_delete=PROTECT, blank=True, null=True)
    residence_all = BooleanField(default=False)
    destination_all = BooleanField(default=False)
    arrival_date = DateTimeField(auto_now_add=True)
    description = TextField(max_length=2000, default='', blank=True)
    pets = BooleanField(default=False)
    pets_description = TextField(max_length=2000, default='', blank=True)
    children_0_4 = IntegerField(default=0)
    children_5_12 = IntegerField(default=0)
    children_12_18 = IntegerField(default=0)
    adults = IntegerField(default=1)
    disabled = IntegerField(default=0)
    attachment_1 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True)

    @property
    def amount_of_people(self):
        return self.children_0_4 + self.children_5_12 + self.children_12_18 + self.adults + self.disabled 
    

class Task(models.Model):
    object_type = IntegerField(default=TASK_GROUP_TYPE)
    name = CharField(max_length=150, blank=False)
    status = ForeignKey(Status, on_delete=PROTECT, default=1)
    description = TextField(max_length=2000, default='', blank=True)
    sender = ForeignKey(User, related_name='related_sender_user', on_delete=PROTECT, blank=True, null=True)
    accepted_by = ForeignKey(User, related_name='related_accepted_by_user', on_delete=PROTECT, blank=True, null=True)
    department = models.ForeignKey(Group, on_delete=PROTECT)
    created_date = DateTimeField(auto_now_add=True)
    modificate_date = DateTimeField(auto_now=True)
    attachment_1 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True)
    attachment_2 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True)
    attachment_3 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True)



