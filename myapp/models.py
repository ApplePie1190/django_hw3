from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
