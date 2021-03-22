from django.contrib import admin
from myapi.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','rollno','name','clas']


# Register your models here.
