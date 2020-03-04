from django.urls import path
from raised import views

urlpatterns = [
        path('raised', views.RaisedPrivate.as_view({
            'post': 'create',
            'put': 'update'}),
            name='raised'
        ),
        path('raised/<int:pk>', views.RaisedPrivate.as_view({
            'get': 'retrieve'}),
            name='raised-detail'
        ),
        path('raised-public/<int:pk>', views.RaisedPublic.as_view({
            'get': 'retrieve'}),
            name='raised-public-detail'
        ),
]
