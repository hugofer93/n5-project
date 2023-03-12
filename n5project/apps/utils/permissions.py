from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def generate_group_permission(group_name):
    """Generate group permission instance.

    Args:
        group_name (str): Group name.

    Returns:
        Group: Group instance.
    """
    UserModel = get_user_model()
    group, _ = Group.objects.get_or_create(name=group_name)
    content_type = ContentType.objects.get_for_model(UserModel)
    permission, _ = Permission.objects.get_or_create(
        codename=f'is_{group_name}',
        name=f'is_{group_name}',
        content_type=content_type)
    group.permissions.add(permission)
    return group
