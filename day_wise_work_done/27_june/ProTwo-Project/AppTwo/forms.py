from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    # For any custom validation, do it here
    class Meta:
        model = User
        fields = '__all__'
