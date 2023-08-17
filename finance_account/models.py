from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

class FinanceAccount(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  username = models.CharField(max_length=50)
  incomes = ArrayField(models.IntegerField(), default=None, blank=True, null=True)
  new_expenses = ArrayField(models.IntegerField(), default=None, blank=True, null=True)
  saved_expense_value = models.IntegerField(default=None)
  
  def __str__(self):
    return self.username