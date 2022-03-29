from django.db.models.base import Model
from django.db.models.fields import Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user','datecreated']

class updateForm(ModelForm):
    class Meta:
        model = order
        fields = ['customer','product','status']
        
class orderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

 