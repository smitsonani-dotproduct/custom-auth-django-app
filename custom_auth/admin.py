from django.contrib import admin
from custom_auth.models import User


@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ["email", "username"]
