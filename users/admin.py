from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('username',)
    search_fields = ('username',)
    readonly_fields = ('password', 'email')
    inlines = (BasketAdmin,)
