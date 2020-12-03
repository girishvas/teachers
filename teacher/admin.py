from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display 	= ('name', 'added_on')
    list_filter 	= ['added_on']
    search_fields 	= ['name']

admin.site.register(Subject, SubjectAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display 	= ('first_name', 'last_name', 'email', 'phone_number', 'room_number', 'added_on')
    list_filter 	= ['added_on']
    search_fields 	= ['first_name', 'last_name', 'email', 'phone_number', 'room_number']
    
admin.site.register(Teacher, TeacherAdmin)