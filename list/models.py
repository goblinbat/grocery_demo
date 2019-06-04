from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grabbed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
