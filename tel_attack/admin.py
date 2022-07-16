from django.contrib import admin

# Register your models here.
from .models import Attack, TelephoneNumber
admin.site.register(Attack)
admin.site.register(TelephoneNumber)
