from django.urls import path
from raised import views

urlpatterns = [
        path('raised', views.RaisedPrivate.as_view({
            'post': 'create',
            'put': 'update'}),
            name='raised'
        ),
]
