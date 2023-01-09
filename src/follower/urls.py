from django.urls import path
from .views import FollowerListView, FollowerView

urlpatterns = [
    path('<int:pk>', FollowerListView.as_view({'get': 'list'})),
    path('user/<int:pk>/', FollowerView.as_view()),
]
