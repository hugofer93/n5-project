from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from n5project.apps.api.auth.permissions import IsOfficerPermission
from n5project.apps.documents.models import Violation
from n5project.apps.api.documents.serializers import (
    CreateViolationSerializer,
    ConsultViolationSerializer,
)


UserModel = get_user_model()


class CreateViolationView(CreateAPIView):
    http_method_names = ['post', ]
    permission_classes = [IsOfficerPermission, ]
    serializer_class = CreateViolationSerializer


class ConsultViolantionView(ListAPIView):
    http_method_names = ['post', ]
    permission_classes = [AllowAny, ]
    serializer_class = ConsultViolationSerializer
    queryset = Violation.objects.all_active()

    def filter_queryset(self, queryset, person_email):
        queryset = super().filter_queryset(queryset)
        queryset = queryset.filter(person__email=person_email)
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person_email = serializer.validated_data.get('email')
        queryset = self.filter_queryset(self.get_queryset(), person_email)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
