from django.db import models

# Create your models here.
class Book (models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    author=models.CharField(max_length =200)
    year_of_publication=models.DateField()
    isAvailable =models.BooleanField()
    count=models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

