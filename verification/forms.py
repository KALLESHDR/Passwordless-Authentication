class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="Enter your phone number here")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_details = User.objects.filter(username=username)
        if user_details.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_details = User.objects.filter(email=email)
        if user_details.exists():
            raise forms.ValidationError("There is already an account with this email , please try logging in!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        user_details = User.objects.filter(phone_number=phone_number)
        if user_details.exists():
            raise forms.ValidationError(
                "An account with this phone number already exists! Please try registering using a different phone number or try logging in!")
        return phone_number

    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="Enter your phone number here")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_details = User.objects.filter(username=username)
        if user_details.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_details = User.objects.filter(email=email)
        if user_details.exists():
            raise forms.ValidationError("There is already an account with this email , please try logging in!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        user_details = User.objects.filter(phone_number=phone_number)
        if user_details.exists():
            raise forms.ValidationError(
                "An account with this phone number already exists! Please try registering using a different phone number or try logging in!")
        return phone_number





class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_details = User.objects.filter(email=email)
        if not user_details.exists():
            raise forms.ValidationError("No account exists with this email. Try registering")
        return email
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="Enter your phone number here")