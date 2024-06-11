from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)
    # Другие поля профиля, которые вам нужны



class CardPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    card_cvv = models.IntegerField()
    expiry_date = models.CharField(max_length=10)