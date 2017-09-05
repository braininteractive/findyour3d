from django import forms

from findyour3d.users.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'user_type')

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.user_type = self.cleaned_data['user_type']
        user.save()
