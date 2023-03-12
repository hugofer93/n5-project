from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    DateTimeField,
    EmailField,
    Serializer,
    UUIDField,
    ValidationError
)

from n5project.apps.core.models import Vehicle
from n5project.apps.documents.models import Violation


UserModel = get_user_model()


class CreateViolationSerializer(Serializer):
    person_id = UUIDField()
    license_plate = CharField(max_length=10, write_only=True)
    datetime = DateTimeField()
    description = CharField(max_length=100)
    comments = CharField(max_length=100, allow_blank=True)

    def validate_person_id(self, value):
        if not UserModel.objects.all_active().filter(id=value).exists():
            raise ValidationError("Person doesn't exist.")
        return value

    def create(self, validated_data):
        try:
            vehicle = Vehicle.objects.all_active().get(
                license_plate=validated_data.get('license_plate'))
        except Vehicle.DoesNotExist:
            raise ValidationError({
                'license_plate': ["Vehicle doesn't exist.", ],
            })
        violation = Violation.objects.create(
            person_id=validated_data.get('person_id'),
            vehicle=vehicle,
            datetime=validated_data.get('datetime'),
            description=validated_data.get('description'),
            comments=validated_data.get('comments'),
        )
        return violation

    def update(self, instance, validated_data):
        raise NotImplementedError


class ConsultViolationSerializer(Serializer):
    email = EmailField(write_only=True)
    id = UUIDField(read_only=True)
    license_plate = CharField(
        max_length=10,
        read_only=True,
        source='violation.vehicle.license_plate')
    description = CharField(max_length=100, read_only=True)
    comments = CharField(max_length=100, allow_blank=True, read_only=True)
    datetime = DateTimeField(read_only=True)

    def validate_email(self, value):
        if not UserModel.objects.all_active().filter(email=value).exists():
            raise ValidationError("Person doesn't exist.")
        return value

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
