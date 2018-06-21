from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.user_name






class FirstSlide(models.Model):
        titles = models.CharField(max_length=200)
        slide_heading=models.CharField(max_length=200)
        width = models.IntegerField(default=0)
        height = models.IntegerField(default=0)
        image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
        upload_time = models.DateTimeField(auto_now_add=True, auto_now=False)
        update_time = models.DateTimeField(auto_now_add=False, auto_now=True)

        def __str__(self):
            return self.titles

        class Meta:
            ordering = ['-upload_time']
            verbose_name_plural = "First Slide"
class Category(models.Model):
    name=models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    category_image = models.ImageField(null=True, blank=True, width_field='width', height_field='height')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Categorie'

class ProductStatus(models.Model):
    product_status=models.CharField(max_length=200)
    def __str__(self):
        return self.product_status

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_status=models.ForeignKey(ProductStatus,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField(default=0)
    product_details=models.TextField(null=True,default='')
    previous_product_price=models.FloatField(default=0)
    product_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.product_name



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    # payment_details = models.ForeignKey(Payment, null=True)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.product_price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)



