from django.db import models

# Create your models here.

class Payment(models.Model):
    email = models.CharField(max_length=50)
    total = models.IntegerField()
    start_month = models.CharField(max_length=10)
    end_month = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.email} paid {self.total} RWF'