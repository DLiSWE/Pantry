from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import EndUser
from django.conf import settings

class UserForm(UserCreationForm):
    class Meta:
        fields = ('first_name','last_name','username','email','phone', 'password1', 'password2')
        model = get_user_model()

class SignupForm(UserForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'
    
class EditForm(UserForm):
    success_url = 'Accounts:prof'
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Change Email Address'
        self.fields['phone'].label = 'Phone Number'

class ProfileUpdateForm(UserForm):
    avatar = forms.ImageField(max_length=300)
    urls = forms.URLField()
    bio = forms.CharField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = get_user_model()
        fields = ['avatar','urls','bio']

    def clean_photo(self):
        photo=self.cleaned_data.get('avatar')
        if photo.size>settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(("{}".format(str(settings.MAX_UPLOAD_SIZE/1000000))))
        return photo
        