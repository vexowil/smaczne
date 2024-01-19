from django.contrib import admin
from .models import Restaurant
from .models import Menu
from .models import User
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(User)