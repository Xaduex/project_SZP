from django.contrib import admin
from .models import Machines, Furnace, Tank, CastingMold, TechSchema, Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(Machines)
admin.site.register(Furnace)
admin.site.register(Tank)
admin.site.register(CastingMold)
admin.site.register(TechSchema)

