from django.db import models

# Create your models here.
class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tenure = models.IntegerField()

from django.contrib.auth.models import User
from django.utils import timezone

class FinanceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link records to users
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.category} - {self.amount}"