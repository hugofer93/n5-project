from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from n5project.apps.api.auth import urls as auth_urls
from n5project.apps.api.documents import urls as documents_urls


app_name = 'api'


urlpatterns = [
    path('auth/', include(auth_urls, namespace='auth')),
    path('documents/', include(documents_urls, namespace='documents')),
]


docs_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]

urlpatterns += docs_urlpatterns
