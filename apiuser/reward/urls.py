from django.urls import path
from reward import views

urlpatterns = [
        path('reward', views.RewardViewSet.as_view({
            'post': 'create',
            'put': 'update',
            'get': 'retrieve',
            'delete': 'destroy'}),
            name='reward'),
        path('reward/<int:pk>', views.RewardViewSet.as_view({
            'get': 'list'}),
            name='display-rewards'
        ),
        path('rewards/<int:pk>', views.RewardPublic.as_view({
            'get': 'list'}),
            name='rewards'
        ),
        path('reward-detail/<int:pk>', views.RewardRetrieve.as_view({
            'get': 'retrieve'}),
            name='reward-detail'
        ),
]
