from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from n5project.apps.core.models import Vehicle


UserModel = get_user_model()


# Custom AdminSite
class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'N5 Admin'
    admin.AdminSite.site_title = admin.AdminSite.site_header


@admin.register(UserModel)
class UserAdmin(DjangoUserAdmin):
    """Custom User Admin for AdminSite"""


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'license_plate',
        'owner_id',
        'brand_name',
        'color',
        'is_active'
    ]
    list_display_link = ['license_plate', ]
    search_fields = ['license_plate', 'owner__id', 'brand_name', 'color']
    list_filter = ['is_active', 'brand_name', 'color', 'creation_date']
