from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    email = models.EmailField()
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.date}"
