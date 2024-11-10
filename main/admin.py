from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_agent', 'scheduled_date', 'scheduled_time', 'status', 'order_date', 'time_remaining', 'weight', 'price', 'payment_status')
    list_filter = ('status', 'user', 'delivery_agent')
    search_fields = ('user__username', 'status', 'delivery_agent__user__username')
    date_hierarchy = 'scheduled_date'
    ordering = ('-order_date',)
    fields = ('user', 'delivery_agent', 'scheduled_date', 'scheduled_time', 'status', 'order_date', 'weight', 'price', 'payment_status','notes')
    readonly_fields = ('order_date',)

admin.site.register(Order, OrderAdmin)

