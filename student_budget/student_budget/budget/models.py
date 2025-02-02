from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=100)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"

from django.db import models
from django.utils import timezone

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    date_spent = models.DateField(null=True)  # Temporarily allow null values

    def __str__(self):
        return f"{self.reason} - {self.amount}"

