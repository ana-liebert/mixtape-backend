from django.contrib import admin

from .models import Mix, Genre, UserProfile, Host

admin.site.register(Mix)
admin.site.register(Genre)
admin.site.register(UserProfile)
admin.site.register(Host)