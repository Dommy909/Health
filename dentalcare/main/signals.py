from django .db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from django.core.mail import send_mail

def send_approval_email(sender, instance, **kwargs):
    if instance.approved:
        send_mail(
            'Appointment Approval',
            f'Daer {instance.patient_name}, your appointment on {instance.date} at
 {instance.time} has been approved.',
 'clinic@example.com',
[instance.email],
        fail_silently=False, 
        )