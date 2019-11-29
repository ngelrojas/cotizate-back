from django.urls import path

from newscampaing import views


urlpatterns = [
        path('news/<int:pk>', views.NewsPrivate.as_view({
            'get': 'list'}),
            name='list-news'
        ),
        path('news', views.NewsPrivate.as_view({
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'}),
            name='news'
        ),
]
