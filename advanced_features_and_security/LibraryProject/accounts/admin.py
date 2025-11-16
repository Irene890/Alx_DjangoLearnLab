from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import User



class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields displayed in admin list view
    list_display = ("username", "email", "date_of_birth", "is_staff")

    # Fields visible when viewing a single user
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fields used when creating a new user in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
