from django.db import models
from django.contrib.auth import get_user_model

class FinanceAccount(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  username = models.CharField(max_length=50)
  income = models.IntegerField(default=0)
  expenses = models.IntegerField(default=0)
  
  def __str__(self):
    return self.username