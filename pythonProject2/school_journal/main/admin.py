from django.contrib import admin

from .models import *

admin.site.register(SchoolSubject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Journal)