
from asyncio.windows_events import NULL
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import AbstractUser, Group
from django.core.mail import send_mail
from django.conf import settings
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
    object_type = IntegerField(unique=True, default=1)
    description = TextField(max_length=2000, default='', blank=True)


    class Meta:
        verbose_name = "Dział"
        verbose_name_plural = "Działy"

class Region(models.Model):
    object_type = IntegerField(default=REGION_GROUP_TYPE)
    name = CharField(unique=True, max_length=150, blank=False)
    code = IntegerField(unique=True, blank=False)
    def __str__(self):
        return self.name


class Status(models.Model):
    object_type = IntegerField(default=STATUS_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, unique=True, verbose_name="Nazwa")

    def __str__(self):
        return self.name

class Voivodeship(models.Model):
    object_type = IntegerField(default=VOIVODESHIP_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, unique=True)
    region = ForeignKey(Region, on_delete=CASCADE)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    username = CharField(max_length=150, blank=False, null=False, unique=True, verbose_name="Nazwa użytkownika")
    city = CharField(max_length=150, blank=True, null=True, verbose_name="Miasto")
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=True, null=True, verbose_name="Województwo")
    phone = CharField(max_length=20, blank=True, null=True, verbose_name="Numer telefonu")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    image = models.ImageField(upload_to='attachments/User/image/', null=True, blank=True, verbose_name="Zdjęcie")

    def __str__(self):
        return self.username

    @property
    def preview(self):
        return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownice"

class Attachment(models.Model):
    object_type = IntegerField(default=ATTACHMENT_GROUP_TYPE)
    object_id = IntegerField(blank=False, null=False)
    name = CharField(max_length=150, blank=False)
    file_object = models.FileField(upload_to='attachments/object_type_{}/object_id_{}/%Y_%m_%d'.format(object_type, object_id))
    created_date = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Załącznik"
        verbose_name_plural = "Załączniki"

class Subgroup(models.Model):
    object_type = IntegerField(default=SUBGROUP_GROUP_TYPE)
    name = CharField(max_length=150, blank=True, null=True, verbose_name="Nazwa")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    department = models.ForeignKey(Department, on_delete=CASCADE, related_name='subgroups', verbose_name="Dział")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Podgrupa"
        verbose_name_plural = "Podgrupy"

class Volunteer(models.Model):
    name = CharField(max_length=150, blank=False, verbose_name="Nazwa")
    another_name = CharField(max_length=150, blank=True, null=True, verbose_name="Nazwa dodatkowa")
    phone = CharField(max_length=150, blank=True, null=True, verbose_name="Kontaktowy numer telefonu")
    email = models.EmailField(max_length=254, blank=True, null=True)
    city = CharField(max_length=150, blank=False, verbose_name="Miasto")
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=False, verbose_name="Województwo")
    created_date = DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    modificate_date = DateTimeField(auto_now=True, verbose_name="Data modyfikacji")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    archives = BooleanField(default=False, verbose_name="Archiwum")
    subgroup = ForeignKey(Subgroup, on_delete=CASCADE, related_name='objects', blank=True, null=True, verbose_name="Podgrupa")
    attachment_1 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True, verbose_name="Załąćznik 1")
    attachment_2 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True, verbose_name="Załąćznik 2")
    attachment_3 = models.FileField(upload_to='attachments/Apartment/{}'.format('_id'), null=True, blank=True, verbose_name="Załąćznik 3")

    def __str__(self):
        return self.name

class Apartment(Volunteer):
    object_type = IntegerField(default=APARTMENT_GROUP_TYPE)
    max_number_of_people = IntegerField(default=0, verbose_name="Maksymalna ilość miejsc")
    current_number_of_people = IntegerField(default=0, verbose_name="Aktualna ilość zajętych miejsc")
    free_space = IntegerField(default=0, verbose_name="Wolne miejsca")
    operating_range = IntegerField(default=0, verbose_name="Zasięg km")
    provides_transportation = BooleanField(default=False, verbose_name="Zapewnia transport")
    available = BooleanField(default=True, verbose_name="Dostępny")
    
    class Meta:
        verbose_name = "Mieszkanie"
        verbose_name_plural = "Mieszkania"

class Transport(Volunteer):
    object_type = IntegerField(default=TRANSPORT_GROUP_TYPE)
    max_number_of_people = IntegerField(default=0, verbose_name="Maksymalna ilość miejsc")
    operating_range = IntegerField(default=0, verbose_name="Zasięg km")
    available = BooleanField(default=True, verbose_name="Dostępny")

    class Meta:
        verbose_name = "Transport"
        verbose_name_plural = "Transporty"

class Collection(Volunteer):
    object_type = IntegerField(default=COLLECTION_GROUP_TYPE)

    class Meta:
        verbose_name = "Zbiórka"
        verbose_name_plural = "Zbiórki"

class Sponsor(Volunteer):
    object_type = IntegerField(default=SPONSOR_GROUP_TYPE)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsorze"

class Media(Volunteer):
    object_type = IntegerField(default=MEDIA_GROUP_TYPE)

class OneOffAction(models.Model):
    object_type = IntegerField(default=ONEOFFACCTION_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, verbose_name="Tytuł")
    department = models.ForeignKey(Group, on_delete=PROTECT, verbose_name="Dział")
    date_start = DateTimeField(auto_now_add=True, verbose_name="Data Początku")
    date_end = DateTimeField(auto_now_add=True, verbose_name="Data Zakończenia")
    city = CharField(max_length=150, blank=False, verbose_name="Miasto")
    voivodeship = ForeignKey(Voivodeship, on_delete=PROTECT, blank=False, verbose_name="Województwo")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    status = ForeignKey(Status, on_delete=PROTECT, default=1, verbose_name="Status")
    max_number_of_people = IntegerField(verbose_name="Maksymalna ilość miejsc")
    current_number_of_people = IntegerField(verbose_name="Akualna ilość zajętych miejsc")
    attachment_1 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 1")
    attachment_2 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 2")
    attachment_3 = models.FileField(upload_to='attachments/OneOffAction/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 3")

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Akcja jednorazowa"
        verbose_name_plural = "Akcje jednorazowe"

class Application(models.Model):
    object_type = IntegerField(default=APPLICATION_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, verbose_name="Nazwa")
    phone = CharField(max_length=20, blank=True, null=True, verbose_name="Kontaktowy numer telefonu")
    department = models.ForeignKey(Department, on_delete=PROTECT, verbose_name="Dział")
    subgroup = ForeignKey(Subgroup, on_delete=CASCADE, related_name='application_objects', blank=True, null=True, verbose_name="Podgrupa")
    volunteer = ForeignKey(Volunteer, on_delete=CASCADE, blank=True, null=True, verbose_name="Wolonter")
    created_date = DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    contactApp = CharField(max_length=200, blank=True, null=True, verbose_name="Aplikacja do kontaktu")
    status = ForeignKey(Status, on_delete=PROTECT, default=1, verbose_name="Status")
    residence_city = CharField(max_length=150, blank=True, null=True, verbose_name="Miasto przebywania")
    residence_voivodeship = ForeignKey(Voivodeship, related_name='related_app_res_voivodeship', on_delete=PROTECT, blank=True, null=True, verbose_name="Województwo przebywania")
    destination_city = CharField(max_length=150, blank=True, null=True, verbose_name="Miasto docelowe")
    destination_voivodeship = ForeignKey(Voivodeship, related_name='related_app_dest_voivodeship', on_delete=PROTECT, blank=True, null=True, verbose_name="Województwo docelowe")
    residence_all = BooleanField(default=False, verbose_name="Lokalizacja - Cały kraj")
    destination_all = BooleanField(default=False, verbose_name="Miejsce docelowe - Cały kraj")
    arrival_date = DateTimeField(auto_now_add=True, verbose_name="Data Przebycia")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    pets = BooleanField(default=False, verbose_name="Zwirzęta domowe")
    pets_description = TextField(max_length=2000, default='', blank=True, verbose_name="Zwirzęta domowe Opis")
    children_0_4 = IntegerField(default=0, verbose_name="Dzieci do 4-ch lat")
    children_5_12 = IntegerField(default=0, verbose_name="Dzieci od 5 do 12-tu lat")
    children_13_17 = IntegerField(default=0, verbose_name="Dzieci od 13 do 17-tu lat")
    adults = IntegerField(default=1, verbose_name="Dorosłe")
    disabled = IntegerField(default=0, verbose_name="Niepełnosprawni")
    attachment_1 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 1")
    attachment_2 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 2")
    attachment_3 = models.FileField(upload_to='attachments/Application/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 3")

    @property
    def amount_of_people(self):
        return self.children_0_4 + self.children_5_12 + self.children_12_18 + self.adults + self.disabled 
    
    class Meta:
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"

class Task(models.Model):
    object_type = IntegerField(default=TASK_GROUP_TYPE)
    name = CharField(max_length=150, blank=False, verbose_name="Tytuł")
    status = ForeignKey(Status, on_delete=PROTECT, default=1, verbose_name="Status")
    description = TextField(max_length=2000, default='', blank=True, verbose_name="Opis")
    sender = ForeignKey(User, related_name='related_sender_user', on_delete=PROTECT, blank=True, null=True, verbose_name="Nadzorujący")
    accepted_by = ForeignKey(User, related_name='related_accepted_by_user', on_delete=PROTECT, blank=True, null=True, verbose_name="Osoba opracująca")
    department = models.ForeignKey(Group, on_delete=PROTECT, verbose_name="Dział")
    created_date = DateTimeField(auto_now_add=True, verbose_name="Data Utworzenia")
    modificate_date = DateTimeField(auto_now=True, verbose_name="Data modyfikacji")
    attachment_1 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 1")
    attachment_2 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 2")
    attachment_3 = models.FileField(upload_to='attachments/Task/{}'.format(id), null=True, blank=True, verbose_name="Załąćznik 3")
    sended_msg = BooleanField(default=False)

    class Meta:
        verbose_name = "Zadanie"
        verbose_name_plural = "Zadania"

    def save(self, *args, **kwargs):
        if self._state.adding == True:
            recipients = User.objects.filter(groups=self.department)
            subject = 'Nowe zadanie od ' + self.sender.username
            message = 'Sprawdż nowe zananie na liście. Nazwa: ' + self.name + ' - ' + self.description
            recipients_list = []
            if self.accepted_by is not None:
                if self.accepted_by.email is not '':
                    recipients_list.append(self.accepted_by.email)
                else:
                    subject = 'Wiadomość o nowym zadaniu nie zostało wysłane do ' + self.accepted_by.username
                    recipients_list.append(self.sender.email)
            else:
                for recipient in recipients:
                    recipients_list.append(recipient.email)
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL , recipients_list, fail_silently = False)
        super().save(*args, **kwargs)



