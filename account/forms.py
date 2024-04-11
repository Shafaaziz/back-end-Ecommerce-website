from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'phone']
    
    def clean_password2(self):
        data = self.cleaned_data
        if data['password2'] != data['password1']:
            raise forms.ValidationError('!گذرواژه‌ها یکسان نیستند')
        return data['password2']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField
    class Meta:
        model = User
        fields = ['email', 'username', 'phone']

    def clean_password(self):
        return self.initial['password']
    
class authForm(forms.Form):
    phone = forms.CharField(max_length=11,min_length=11)

class ProfileForm(forms.Form):
    username = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    email = forms.EmailField()
    address = forms.Textarea()
    IP_address = forms.IntegerField()

class Update_ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone','email','address','IP_address']


