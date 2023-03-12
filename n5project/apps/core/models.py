from uuid import uuid4

from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, PROTECT, UUIDField

from n5project.apps.core.managers import UserManager
from n5project.apps.utils.models import BaseUUIDModel
from n5project.apps.utils.permissions import generate_group_permission


class User(AbstractUser):
    """Custom User Model"""
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    objects = UserManager()


class Vehicle(BaseUUIDModel):
    brand_name = CharField(max_length=20)
    color = ColorField()
    license_plate = CharField(max_length=10, unique=True)
    owner = ForeignKey(User, on_delete=PROTECT)
