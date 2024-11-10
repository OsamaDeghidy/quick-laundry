from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.validators import RegexValidator



from django import forms
from django.core.validators import RegexValidator
from .models import UserProfile
from django import forms
from django.core.validators import RegexValidator
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', )
        widgets = {
            
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Name'}),
            }
class UserProfileForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. the number must be 10 digits."
    )
    phone_number = forms.CharField(
        validators=[phone_regex],
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '+999999999', 'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ( 'phone_number', 'house_number', 'street_name', 'street_number', 'postal_code', 'area')
        widgets = {
            
            'house_number': forms.TextInput(attrs={'placeholder': 'House/Apt Number', 'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'placeholder': 'Street Name', 'class': 'form-control'}),
            'street_number': forms.TextInput(attrs={'placeholder': 'Street Number', 'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code', 'class': 'form-control'}),
            'area': forms.TextInput(attrs={'placeholder': 'Area', 'class': 'form-control'}),
        }



        
# from myjop.models import *
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from myjop.models import UserProfile

# class SignUpForm(UserCreationForm):
#     role = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('employer', 'Medical center')])
#     member_number = forms.CharField(max_length=15, required=False, label='Mobile Number')

#     class Meta:
#         model = User
#         fields = ( 'role','member_number','username', 'password1', 'password2',)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('role',)

# class DoctorProfileForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['specialization', 'contact_number', 'whats_num', 'profile_picture', 'decrp']

# class EmployerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Employer
#         fields = ['contact_number', 'profile_picture', 'name_hospital', 'address_hospital', 'contact_number_hospital']


# # forms.py


# class EmployerProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Employer
#         fields = ['contact_number', 'profile_picture', 'name_hospital', 'address_hospital', 'contact_number_hospital']
#         labels = {
#             'contact_number': 'رقم الاتصال:',
#             'profile_picture': 'صورة الملف الشخصي:',
#             'name_hospital': 'اسم  المركز /العيادة:',
#             'address_hospital': 'عنوان المركز /العيادة:',
#             'contact_number_hospital': 'رقم الاتصال المركز /العيادة:'
#         }

#     def __init__(self, *args, **kwargs):
#         super(EmployerProfileEditForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

# class DoctorProfileEditForm(forms.ModelForm):
#     profile_picture = forms.ImageField(label='صورة الملف الشخصي:',required=False)
#     class Meta:
#         model = Doctor
#         fields = ['name','specialization', 'contact_number', 'whats_num', 'profile_picture', 'decrp']
#         labels = {
#             'name': 'الاسم:',
#             'specialization': 'التخصص:',
#             'contact_number': 'رقم الاتصال:',
#             'whats_num': 'رقم WhatsApp:',
#             'profile_picture': 'صورة الملف الشخصي:',
#             'decrp': 'الوصف:'
#         }
#     def __init__(self, *args, **kwargs):
#         super(DoctorProfileEditForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

from django import forms
from django.contrib.auth.models import User
from .models import DeliveryAgent

class DeliveryAgentSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class DeliveryAgentProfileForm(forms.ModelForm):
    class Meta:
        model = DeliveryAgent
        fields = ['phone_number', 'address']
