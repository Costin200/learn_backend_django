from django.urls import path

from . import views

urlpatterns = [
    path('product', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
    path('orderline', views.OrderLineList.as_view()),
    path('orderline/<int:pk>', views.OrderLineDetail.as_view()),
    path('order', views.OrderList.as_view()),
    path('order/<int:pk>', views.OrderDetail.as_view()),
]
