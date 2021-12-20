from django.contrib import admin
from .models import Owner, Unit, UnitOwner

# Register your models here.
admin.site.register(Owner)
admin.site.register(Unit)
admin.site.register(UnitOwner)


