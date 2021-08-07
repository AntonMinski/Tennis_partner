from django_registration.forms import RegistrationForm
from .models import BaseUser


class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = BaseUser