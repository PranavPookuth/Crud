from django.urls import path
from .views import ProductsView,ProductsViewById

urlpatterns=[
    path('products/',ProductsView.as_view()),
    path('products/<int:id>/',ProductsViewById.as_view(),)
]