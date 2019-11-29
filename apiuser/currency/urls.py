from django.urls import path
from currency import views

urlpatterns = [
        path('currency', views.CurrencyPublic.as_view({
            'get': 'list'}),
            name='currency'),
]
