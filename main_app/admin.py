from django.contrib import admin

# Register your models here.
from .models import Finch

#allows full CRUDding in our admin app for finch table in db
admin.site.register(Finch)