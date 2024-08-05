from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreatinForm, CustomUserChangeForm

# Register your models here.



class CustomUserAdmin(UserAdmin):
    #creation new user "from doc."

    add_form = CustomUserCreatinForm
    #from doc
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username","email","first_name","last_name","password"]



admin.site.register(CustomUser, CustomUserAdmin)
