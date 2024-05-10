from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # password = models.CharField(max_length=100)
    t_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=100)
    date_reg = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, tel:{self.t_number}'

    class Meta:
        verbose_name = "Client name"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category name"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name="Photo")

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def __str__(self):
        return f'{self.name} / {self.category} / {self.price}'

    class Meta:
        verbose_name = "Product name"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_prod = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def get_absolute_url(self):
        return reverse('order', kwargs={'product_id': self.pk})

    def __str__(self):
        return f'Name is {self.customer.name} order is {self.products.name}'


    @property
    def get_summary(self):
        return f'summa of order = {sum(product.price*product.quantity for product in Product.objects.all())}'


