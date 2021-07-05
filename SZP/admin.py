from django.contrib import admin
from .models import User, Machines, Furnace, Tank, CastingMold, TechSchema

# Register your models here.

admin.site.register(User)
admin.site.register(Machines)
admin.site.register(Furnace)
admin.site.register(Tank)
admin.site.register(CastingMold)
admin.site.register(TechSchema)

