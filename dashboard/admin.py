from django.contrib import admin
from .models import SalesReport

@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'report_date', 'total_amount']
    list_filter = ['report_date']
