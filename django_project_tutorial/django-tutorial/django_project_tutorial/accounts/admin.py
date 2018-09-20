from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
# admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')


    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)

        queryset = queryset.order_by('-phone', 'user') # do phone to in reverse order !, the second parameter is a fallback parameter, final one is the order in which it was inserted

        return queryset


    user_info.short_description = 'Info'


admin.site.register(UserProfile, UserProfileAdmin)
