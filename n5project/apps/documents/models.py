from django.contrib.auth import get_user_model
from django.db.models import CharField, DateTimeField, ForeignKey, PROTECT

from n5project.apps.core.models import Vehicle
from n5project.apps.utils.models import BaseUUIDModel


UserModel = get_user_model()


class Violation(BaseUUIDModel):
    person = ForeignKey(UserModel, on_delete=PROTECT)
    vehicle = ForeignKey(Vehicle, on_delete=PROTECT)
    description = CharField(max_length=100)
    comments = CharField(max_length=100, blank=True)
    datetime = DateTimeField()


class Citation(BaseUUIDModel):
    person = ForeignKey(UserModel, on_delete=PROTECT)
    vehicle = ForeignKey(Vehicle, on_delete=PROTECT)
    description = CharField(max_length=100)
    comments = CharField(max_length=100, blank=True)
    datetime = DateTimeField()
