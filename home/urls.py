from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('',views.HomeView.as_view(),name='home'),
path('category/<category>',views.CategoryView.as_view(),name='category'),
path('signup/',views.SignUp.as_view(),name='signup'),
path('login/',auth_views.login, {'template_name': 'login.html'},name='login'),
path('add-to-cart/',views.add_to_cart,name='cart'),
path('checkout/',views.checkout,name='checkout'),
path('order_summary/',views.order_details,name='order_summary'),
path('delete_item/<item_id>',views.delete_from_cart,name='delete_item'),
path('shop/',views.ShopList.as_view(),name='shop'),
path('product_details/<int:pk>',views.ProductDetail.as_view(),name='product_details')
]


if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)