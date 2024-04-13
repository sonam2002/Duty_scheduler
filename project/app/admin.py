from django.contrib import admin
from .models import  DutySchedule

@admin.register(DutySchedule)
class DutyScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','day', 'shift', 'doctor_name')
   
