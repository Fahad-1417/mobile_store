from django.db import models
from checkout.models import Order

class SalesReport(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Report #{self.id} - {selfreport_date.date()}"
