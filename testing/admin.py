from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image')

    def user_info(self, obj):
        return obj.UserProfile.user
admin.site.register(UserProfile, UserProfileAdmin)