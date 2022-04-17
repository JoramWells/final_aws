from django.contrib import admin

# Register your models here.\
from .models import *
admin.site.register(Pepper)
admin.site.register(Tomato)
admin.site.register(Potato)

admin.site.register(PepperDiseases)
admin.site.register(TomatoDiseases)
admin.site.register(PotatoDiseases)


