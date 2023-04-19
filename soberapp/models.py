from django.db import models

# Create your models here.
class Human(models.Model):
    phone=models.CharField(max_length=50, unique=True)
    days=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.phone} wants {self.days} days'

class Track(models.Model):
    human=models.ForeignKey(Human, on_delete=models.CASCADE)
    date_taken=models.CharField(max_length=25)
    achieved=models.BooleanField()
    note=models.TextField()

    def __str__(self) -> str:
        return f'{self.human.phone} ... {self.achieved}'


