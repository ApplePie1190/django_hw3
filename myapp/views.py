from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import User, Product, Order
import logging


logger = logging.getLogger(__name__)


def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer_id=user)
    return render(request, 'myapp/user_orders.html', {'user': user, 'orders': orders})


def sort_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)
    
    orders_last_week = Order.objects.filter(customer_id=user, date_ordered__gte=last_week)
    orders_last_month = Order.objects.filter(customer_id=user, date_ordered__gte=last_month)
    orders_last_year = Order.objects.filter(customer_id=user, date_ordered__gte=last_year)
    
    products_last_week = Product.objects.filter(order__in=orders_last_week).distinct()
    products_last_month = Product.objects.filter(order__in=orders_last_month).distinct()
    products_last_year = Product.objects.filter(order__in=orders_last_year).distinct()

    context = {
        'user': user,
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }
    
    return render(request, 'myapp/sort_products.html', context)