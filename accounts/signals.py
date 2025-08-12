from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from accounts.models import CompanyProfile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CompanyProfile.objects.create(user=instance)


@receiver(post_migrate)
def create_default_admin_groups(sender, **kwargs):
    super_admin_group, _ = Group.objects.get_or_create(name='Super Admins')
    if not super_admin_group.permissions.exists():
        perms = Permission.objects.all()
        super_admin_group.permissions.set(perms)

    staff_admin_group, _ = Group.objects.get_or_create(name='Staff Admins')
    if not staff_admin_group.permissions.exists():
        perms = Permission.objects.filter(codename__in=[
            'add_companyprofile',
            'change_companyprofile',
            'view_companyprofile',
            'add_employee',
            'change_employee',
            'view_employee',
            'add_project',
            'change_project',
            'view_project',
        ])
        staff_admin_group.permissions.set(perms)