from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListApiView.as_view(), name = 'product_list'),
    path('product_detail/<str:slug>/', views.ProductDetailApiView.as_view(), name = 'product_detail'),

]