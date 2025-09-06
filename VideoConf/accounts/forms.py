from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            get_user_model().USERNAME_FIELD,
            'password1',
            'password2'
        )
