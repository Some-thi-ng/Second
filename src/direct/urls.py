from django.urls import path
from .views import DialogListView, MessageView, CreateDialogView, DialogView

urlpatterns = [
    path('all', DialogListView.as_view({'get': 'list'})),
    path('send/<int:pk>', CreateDialogView.as_view()),
    path('<int:pk>', DialogView.as_view({'get': 'retrieve'})),
    path('message/send', MessageView.as_view({'post': 'create'})),
    path('message/<int:pk>', MessageView.as_view({'get': 'retrieve'})),
]
