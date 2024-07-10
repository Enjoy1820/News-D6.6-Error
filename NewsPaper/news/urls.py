from django.urls import path

from .views import Postlist, PostDetail

urlpatterns = [
    path('', Postlist.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]