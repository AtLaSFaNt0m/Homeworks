from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин", required=True)
    password = forms.CharField(min_length=8, label="Введите пароль", widget=forms.PasswordInput, required=True)
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль", widget=forms.PasswordInput, required=True)
    age = forms.IntegerField(max_value=99, label="Введите свой возраст", required=True)
