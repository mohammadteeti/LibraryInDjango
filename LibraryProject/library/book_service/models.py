from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Book (models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    author=models.CharField(max_length =200)
    image=models.FileField()
    year_of_publication=models.DateField()
    isAvailable =models.BooleanField()
    count=models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
  books=models.ManyToManyField('Book',related_name='books')
  ordered_on=models.DateField(auto_now_add=True)
  

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    orderes=models.ManyToManyField('Order',related_name='orderes')
    
    def __str__(self):
        return self.user.username
  
class Category (models.Model):
    #Books should be in DB even after category remove
    books = models.ForeignKey('Books',related_name='books',on_delete=models.DO_NOTHING)
    name =models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

    



