from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# TODO форма регистрации
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# TODO форма авторизации
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# TODO форма заказа
class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.IntegerField(label='Номер телефона (в формате +375ххххххххх)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    coment = forms.CharField(label='Комментарий к заказу', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)