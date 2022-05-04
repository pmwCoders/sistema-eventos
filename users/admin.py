from django.contrib import admin
from .models import (
    User,
    EstudanteProfile,
    VisitanteProfile
)
from django.contrib.auth.models import Permission

admin.site.register(User)
admin.site.register(EstudanteProfile)
admin.site.register(VisitanteProfile)
