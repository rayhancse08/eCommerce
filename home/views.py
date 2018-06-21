from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import FirstSlide,Category,Product,Profile,User,OrderItem, Order
from django.shortcuts import get_list_or_404
from .forms import SignupForm
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Count
# Create your views here.

class BaseHTML(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_item'] = OrderItem.objects.all().count()
        return context


class HomeView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_slide']=FirstSlide.objects.all()
        context['categories']=Category.objects.all()
        context['category_wise']=Product.objects.filter(product_status__product_status='New Arival').order_by('category')
        context['distinct_category']=context['category_wise'].distinct('category')
        context['order_item']=OrderItem.objects.all().count()
        return context

class CategoryView(ListView):
    #slug_field = 'category__name'
    #queryset = Product.objects.filter(category__name='MEN')
    template_name = 'category.html'
    #slug_field = 'category__name'
    context_object_name = 'product_category'

    def get_queryset(self):
        self.category = get_list_or_404(Product, category__name=self.kwargs['category'])
        return self.category


class SignUp(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse('home')

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product_id=request.POST['product_id']
    #product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    product=Product.objects.filter(id=product_id).first()
    # check if the user already owns this product
    if product in request.user.profile.product.all():
        messages.info(request, 'You already own this ebook')
        #return redirect(reverse('home'))
        return HttpResponse('')
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    #if status:
        # generate a reference code
        #user_order.ref_code = generate_order_id()
        #user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    #return redirect(reverse('home'))
    #return redirect(reverse('home'))
    return HttpResponse('')
@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('order_summary'))


@login_required()
def order_details(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'checkout.html', context)



class ShopList(ListView):
    template_name = 'shop.html'
    #context_object_name = 'shop_list'
    model = Product
    paginate_by = 10
    #paginator = Paginator(Product, 20)
    def get_context_data(self, **kwargs):
        context = super(ShopList, self).get_context_data(**kwargs)
        product = Product.objects.all()
        paginator = Paginator(product, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)

        context['shop_list'] = product_list
        return context

class ProductDetail(DetailView):
    template_name = 'product_details.html'
    model=Product
    context_object_name = 'product_details'


