from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transactions(models.Model):
    TRANSACTION_TYPES = (
        (1, 'Income'),
        (-1, 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=TRANSACTION_TYPES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
