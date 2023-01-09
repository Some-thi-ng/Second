from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# SWAGGER
schema_view = get_schema_view(
    openapi.Info(
        title='Linked Api',
        default_version='v1',
        description='Rest-API социальной сети',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('src.account.urls')),
    path('gallery/', include('src.gallery.urls')),
    path('followers/', include('src.follower.urls')),
    path('feed/', include('src.feed.urls')),
    path('direct/', include('src.direct.urls')),
    # Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
