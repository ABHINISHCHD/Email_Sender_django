from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(staff)
class Staffs(admin.ModelAdmin):
    list_display=['id','name','email','position','address','phone']

@admin.register(student)
class Students(admin.ModelAdmin):
    list_display=['id','name','email','address','phone']