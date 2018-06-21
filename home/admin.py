from django.contrib import admin
from .models import FirstSlide,Category,Product,ProductStatus,User,Profile
from .models import OrderItem, Order #, PaymentMethod, Payment


# Register your models here.
admin.site.register(FirstSlide)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductStatus)
admin.site.register(User)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Profile)