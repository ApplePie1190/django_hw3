from django.urls import path
from .views import user_orders, sort_products


urlpatterns = [
    path('user_orders/<int:user_id>', user_orders, name='user_orders'),
    path('sort_products/<int:user_id>', sort_products, name='sort_products'),
]
