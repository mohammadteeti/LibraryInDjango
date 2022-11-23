from django.contrib import admin
from book_service.models import Book,Profile,Order
from django.contrib.auth.models  import User,Group
from django.db import models
from django.contrib.admin import ModelAdmin


# Register your models here.
admin.site.register(Book)
admin.site.unregister(Group)
admin.site.register(Order)

class ProfileInline(admin.StackedInline):
    model=Profile
    
    
class UserAdmin(admin.ModelAdmin):
    model=User
    
    inlines=[ProfileInline]
    
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

