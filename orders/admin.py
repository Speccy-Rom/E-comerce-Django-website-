from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email',
                    'address', 'phone', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    readonly_fields = ('id', 'username', 'first_name', 'last_name', 'email',
                       'address', 'phone', 'city',)


admin.site.register(Order, OrderAdmin)
