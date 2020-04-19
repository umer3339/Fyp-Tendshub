from django.contrib import admin
from algo.models import Feedback,ContactForm,SearchForm
from django.contrib.auth.models import auth,User

# Register your models here.
admin.site.register(Feedback)
admin.site.register(ContactForm)
admin.site.register(SearchForm)