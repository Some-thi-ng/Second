from django.urls import path
from .views import PublicationListView, PublicationView, CommentView

urlpatterns = [
    path('<int:pk>', PublicationListView.as_view({'get': 'list'})),
    path('publication', PublicationView.as_view({'post': 'create'})),
    path('publication/<int:pk>', PublicationView.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'destroy'
    })),
    path('publication/<int:pk>/like', PublicationView.as_view({'post': 'like'})),
    path('publication/<int:pk>/unlike', PublicationView.as_view({'post': 'unlike'})),
    path('publication/<int:pk>/fans', PublicationView.as_view({'get': 'fans'})),
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'destroy'
    })),
]
