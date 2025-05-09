from finalProject.professionals.models import Professional


def get_user_obj():
    return Professional.objects.first()