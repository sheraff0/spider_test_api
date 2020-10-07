from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fs = UserAdmin.fieldsets
    fieldsets = (
        fs[0],
        (fs[1][0], {'fields': (*fs[1][1]['fields'], 'phone')}),
        *fs[2:]
    )
