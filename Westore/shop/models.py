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
    def __str__(self):
        return f"{self.name},{self.price},{self.category}"

class Customer(models.Model):
    User_name =models.CharField(max_length=40,unique=True)
    First_name =models.CharField(max_length=40)
    last_name =models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    password = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.User_name},{self.email},{self.mobile},{self.password}"

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.customer.User_name},{self.product.name},{self.quantity}"



