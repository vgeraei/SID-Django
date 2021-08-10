from django.contrib import admin

from django.contrib import admin
from .models import TestSubject, SleepLevelLog, SingleLog

admin.site.register(TestSubject)
admin.site.register(SleepLevelLog)
admin.site.register(SingleLog)