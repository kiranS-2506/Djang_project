from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to="images")
    desc = models.TextField()
    price = models.IntegerField()



