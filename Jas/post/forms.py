from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

from post.models import Comment, Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }


class NewCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write comment'}),
                           required=True)

    class Meta:
        model = Comment
        fields = ("body",)

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

    def clean(self):
        super(UserCreationForm, self).clean()

        # getting username and password from cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # validating the username and password
        if len(username) < 5:
            self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

        if len(password) < 8:
            self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

        return self.cleaned_data


class NewPostform(forms.ModelForm):
    # content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    picture = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Tags | Seperate with comma'}), required=True)

    class Meta:
        model = Post
        fields = ['picture', 'caption', 'tags']
