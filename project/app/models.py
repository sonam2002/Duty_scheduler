from django.db import models
class DutySchedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Night', 'Night')
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    doctor_name = models.CharField(max_length=100)