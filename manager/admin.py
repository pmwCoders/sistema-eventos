from django.contrib import admin

from .models import (
    Evento,
    Presenca
)

admin.site.register(Evento)
admin.site.register(Presenca)