from django.contrib import admin

from .models import Detail

from . import views


# Register your models here.
admin.site.register(Detail)