from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Comment)
# admin.site.register(Reply)
admin.site.register(Solution)
admin.site.register(Liked_by)
