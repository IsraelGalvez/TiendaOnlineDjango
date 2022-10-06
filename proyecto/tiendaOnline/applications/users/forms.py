from django import forms
from .models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):

    username = forms.CharField(
        required = True,
        label= "",
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Email',
            }
        )
    )

    password = forms.CharField(
        required = True,
        label= "",
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Password',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('El usuario o contrasena no son correctos')
        return self.cleaned_data

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Username',
            }
        )
    )

    email = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Email',
            }
        )
    )

    nombres = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Name',
            }
        )
    )

    apellidos = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Last name',
            }
        )
    )

    password1 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Password',
            }
        )
    )
    password2 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Repetir Password',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contrasenas no coinciden')
        else:
            if len(self.cleaned_data['password2']) <= 5:
                self.add_error('password2', 'La contrasena debe tener mas de 5 digitos')

class CambiarContrasena(forms.Form):

    password1 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Contrasena actual',
                'class':'form-control mb-2' 
            }
        )
    )

    password2 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Contrasena nueva',
                'class':'form-control mb-2' 
            }
        )
    )

    password3 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder':'Confirmar contrasena nueva',
                'class':'form-control mb-2' 
            }
        )
    )

    def clean_password3(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password3', 'Las contrasenas nuevas no coinciden')
        else:
            if len(self.cleaned_data['password3']) <= 5:
                self.add_error('password2', 'La contrasena debe tener mas de 5 digitos')