from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.auth.models import auth,User

# Register your models here.

admin.site.site_header = "TrendsHub"
admin.site.site_title = "TrendsHub Admin Portal"
admin.site.index_title = "Welcome to TrendsHub Portal"

admin.site.register(UserProfile)