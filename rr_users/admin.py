from django.contrib import admin

# Register your models here.
from rr_users.models import RR_User

admin.site.register(RR_User)