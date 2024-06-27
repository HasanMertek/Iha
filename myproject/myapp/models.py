from django.db import models
from django.contrib.auth.models import User

class IHA(models.Model):
    isim = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    saatlik_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    mevcut = models.BooleanField(default=True)

    def __str__(self):
        return self.isim

class Rental(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    baslangic_saati = models.DateTimeField()
    bitis_saati = models.DateTimeField()

    def __str__(self):
        return f"{self.iha.isim} rented by {self.user.username}"

class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    iha = models.ForeignKey(IHA, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
