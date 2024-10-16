from django.contrib import admin

from .models import UserProfile, DeliveryAgent

# Register your models here.
admin.site.register(UserProfile)

# Register DeliveryAgent model
@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'is_approved')
    search_fields = ('user__username', 'phone_number', 'address')
    list_filter = ('is_approved',)