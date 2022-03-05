from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django import forms

from .models import User, Department, Subgroup, Region, Voivodeship, Volunteer, Apartment, Status, Application, Transport, Task, OneOffAction

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

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city', 'voivodeship', 'phone', "description", 'image',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('city', 'voivodeship', 'phone', "description",)}),
    )
    list_display = UserAdmin.list_display + ('city', 'voivodeship', 'phone', )
    list_filter = UserAdmin.list_filter + ('city', 'voivodeship', )
    readonly_fields = ('preview',)   

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Zdjęcie'
    thumbnail_preview.allow_tags = True

        
class DepartmentAdmin(GroupAdmin):
    list_display = ("name", "object_type", 'description')
    readonly_fields = ('object_type',)

class SubgroupAdmin(admin.ModelAdmin):
    list_display = ("name", "department", 'description')
    readonly_fields = ('object_type',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    readonly_fields = ('object_type',)

class VoivodeshipAdmin(admin.ModelAdmin):
    list_display = ("name", "region")
    readonly_fields = ('object_type',)

class SubgroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    readonly_fields = ('object_type',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)

class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'the number of vacancies'
    parameter_name = 'free_space'

    def lookups(self, request, model_admin):
        return (
            ('10', '10'),
            ('25', '25'),
            ('50', '50'),
            ('100', '100'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '10':
            return queryset.filter(free_space__gt=10)
        elif value == '25':
            return queryset.filter(free_space__gt=25)
        elif value == '50':
            return queryset.filter(free_space__gt=50)
        elif value == '100':
            return queryset.filter(free_space__gt=100)
        return queryset

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "free_space", "max_number_of_people", "current_number_of_people", "provides_transportation", "city", "voivodeship", "description", "available") 
    list_filter = ("available", IsVeryBenevolentFilter, "city", "voivodeship", "name",) 
    readonly_fields = ('object_type',)
    
    def save_model(self, request, obj, form, change):
        obj.free_space = obj.max_number_of_people - obj.current_number_of_people
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subgroup":
            a_post = Department.objects.get(object_type=APARTMENT_GROUP_TYPE)
            subgroups = a_post.subgroups.all()
            kwargs["queryset"] = subgroups.order_by('name')
        return super(ApartmentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TransportAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "max_number_of_people", "city", "voivodeship", "description", "available") 
    list_filter = ("available", "name", "city", "voivodeship", ) 
    readonly_fields = ('object_type',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subgroup":
            a_post = Department.objects.get(object_type=TRANSPORT_GROUP_TYPE)
            subgroups = a_post.subgroups.all()
            kwargs["queryset"] = subgroups.order_by('name')
        return super(TransportAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "city", "voivodeship", "description") 
    list_filter = ("name", "city", "voivodeship", ) 
    readonly_fields = ('object_type',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subgroup":
            a_post = Department.objects.get(object_type=COLLECTION_GROUP_TYPE)
            subgroups = a_post.subgroups.all()
            kwargs["queryset"] = subgroups.order_by('name')
        return super(CollectionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class SponsorsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "city", "voivodeship", "description") 
    list_filter = ("name", "city", "voivodeship", ) 
    readonly_fields = ('object_type',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subgroup":
            a_post = Department.objects.get(object_type=SPONSOR_GROUP_TYPE)
            subgroups = a_post.subgroups.all()
            kwargs["queryset"] = subgroups.order_by('name')
        return super(SponsorsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "city", "voivodeship", "description") 
    list_filter = ("name", "city", "voivodeship", ) 
    readonly_fields = ('object_type',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subgroup":
            a_post = Department.objects.get(object_type=MEDIA_GROUP_TYPE)
            subgroups = a_post.subgroups.all()
            kwargs["queryset"] = subgroups.order_by('name')
        return super(SocialMediaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class OneOffActionAdmin(admin.ModelAdmin):
    list_display = ("status", "name", "date_start", "date_end", "city", 'voivodeship', "description")
    list_filter = ("status", "name", "date_start", "date_end", "city", 'voivodeship',)
    readonly_fields = ('object_type',)

# def tagform_factory(filetype):
#     class TagForm(forms.ModelForm):
#         m_file = forms.ModelChoiceField(
#             queryset=Volunteer.objects.filter(type_of_help=filetype)
#         )
#     return TagForm

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("department", "name", "phone", "amount_of_people", "created_date", "status", "residence_city", "destination_city", "arrival_date", "description", )
    list_filter = ('department', 'name', 'status', 'created_date', 'residence_city', 'destination_city', 'arrival_date', )
    readonly_fields = ('object_type',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("department", "name", "status", "sender", "accepted_by", "description", "created_date", "modificate_date")
    list_filter = ('department', 'status', 'accepted_by', 'created_date', 'name')
    
    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = ('sender', 'object_type')
        if getattr(obj, 'sender', None) is not None:
            return self.readonly_fields + ('accepted_by',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if obj.status.id == 2: # Jeśli jest w trakcie obróbki z aktualizować użytkownika
            obj.accepted_by = request.user
        if getattr(obj, 'sender', None) is None:
            obj.sender = request.user
        obj.save()



admin.site.register(User, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subgroup, SubgroupAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Voivodeship, VoivodeshipAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(OneOffAction, OneOffActionAdmin)
admin.site.register(Task, TaskAdmin)