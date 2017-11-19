from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

# Register your models here.
# bisa untuk mendaftarkan model disini pada interface admin

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
