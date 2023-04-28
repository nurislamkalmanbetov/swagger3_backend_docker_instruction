from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):  # used to format in console
    list_display = (
        "id",
        "email",
        "username",
        "phone",
        "first_name",
        "last_name",
        "middle_name",
        "role",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )

    readonly_fields = ("date_joined", "last_login")
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
