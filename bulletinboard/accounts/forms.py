from django import forms
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name')


class AuthForm(forms.Form):
    code = forms.IntegerField(label="Registration code")


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        UsersAuth = Group.objects.get(name='AuthUsers')
        UsersAuth.user_set.add(user)
        return user
