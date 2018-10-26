"""
Admin models and registrations for app: accounts
----------------
Registrations: |
----------------
- ProfileInline: for importing Profile model
- CustomUserAdmin: for aligning inlines to admin section

Developer: Anway Somani

"""
# Imports:-
# ---------------------------------------------
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
# ----------------------------------------------

# Inline Properties
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# UserAdmin block
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Unregistering existing...and updating defined
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# View and import Custom User Permissions
from django.contrib.auth.models import Permission
admin.site.register(Permission)
