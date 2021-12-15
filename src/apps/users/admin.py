from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin page"""

    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')

