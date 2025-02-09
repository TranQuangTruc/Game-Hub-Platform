from django.contrib import admin
from django.contrib import admin
from .models import Ticket, TicketResponse

class TicketResponseInline(admin.TabularInline):
    model = TicketResponse
    extra = 0

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'status', 'created_at']
    inlines = [TicketResponseInline]

@admin.register(TicketResponse)
class TicketResponseAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'created_at']
# Register your models here.
