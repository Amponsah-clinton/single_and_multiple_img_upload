from django.forms import ModelForm
from .models import User


# one to one form
class UserForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = User
