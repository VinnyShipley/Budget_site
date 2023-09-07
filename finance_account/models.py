from django.db import models

class FinanceAccount(models.Model):
  name = models.CharField(max_length=100)
  income = models.DecimalField(max_digits=10, decimal_places=2)
  expenses = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name

from django.db import models

