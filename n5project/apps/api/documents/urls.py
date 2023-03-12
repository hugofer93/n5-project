from django.urls import path

from n5project.apps.api.documents.views import (
    CreateViolationView,
    ConsultViolantionView,
)


app_name = 'documents'


urlpatterns = [
    path(
        'violations/',
        CreateViolationView.as_view(),
        name='charge-violation'),
    path(
        'violations/consult/',
        ConsultViolantionView.as_view(),
        name='consult-violation'),
]
