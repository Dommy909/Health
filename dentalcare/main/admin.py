from django.contrib import admin
from .models import Appointment
from django.core.mail import send_mail
from django.conf import settings


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'date', 'is_approved')
    list_editable = ('is_approved',)
    actions = ['approve_appointments']


def approve_appointments(self, request, queryset):
    for appointment in queryset:
        if not appointment.is_approved:
            appointment.is_approved = True
            appointment.save()
            send_mail(
                subject='Appointment Approved',
                message=f"Dear{appointment.patient_name}, your appointment on{appointment.date} has been approved.",)
        self.message_user(request, "Selected appointments approved and notified by email.")
        approve_appointments.short_description = "Approve selected appointments and send email"