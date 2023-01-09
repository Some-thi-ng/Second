from django.urls import path
from .views import (
    CustomUserPublicView, 
    CustomUserView, 
    CustomUserListView,
)

urlpatterns = [
    path('profiles', CustomUserListView.as_view({'get': 'list'})),
    path('public/<int:pk>', CustomUserPublicView.as_view({'get': 'retrieve'})),
    path('profile/<int:pk>', CustomUserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
