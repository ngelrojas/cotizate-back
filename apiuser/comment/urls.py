from django.urls import path
from comment import views

urlpatterns = [
        path('comment', views.CommentPrivate.as_view({
            'get': 'list',
            'post': 'create',
            'put': 'update'}),
            name='list-comment'),
        path('comment/<int:pk>', views.SubCommentPublic.as_view({
            'get': 'retrieve'}),
            name='public-comments'
        ),
        path('subcomment', views.SubCommentPrivate.as_view({
            'post': 'create',
            'put': 'update'}),
            name='subcomment'
        ),
]
