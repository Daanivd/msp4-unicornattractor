from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts.models import Profile


class LoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
class UserRegoForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']    
        
        
    def clean_email(self):
        """"Check if new user doesn't already have a user account (using email address)"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email


    def clean_password2(self):
        """Password validation for password 1 and 2"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2    
   
        
class ProfileForm(forms.ModelForm): 
    """Form to fill in profile information"""
    class Meta:
        model = Profile
        fields = ['info', 'photo']
 
    
class UserForm(forms.ModelForm):
    """Form to fill in additional user information"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']   
  