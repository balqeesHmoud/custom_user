from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreatinForm(UserCreationForm):


    #we can add the rolse here for registration "we have a build in method for this acction"
    class Meta:
        model = CustomUser
        #spesifi the fields that i want to take it from buildin user table
        fields = ("username","email","first_name","last_name")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        #spesifi the fields that i want to take it from buildin user table
        fields = ("username","email","first_name","last_name")
