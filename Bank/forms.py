from django.contrib import admin
from Bank.models import Profile, Deposits, Account
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
        }),
    )


class DateInput(forms.DateInput):
    input_type = 'date'


class BasicForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {'birth_date': DateInput, 'data_vidachi': DateInput, 'sex': forms.RadioSelect,
                   'seria_pasporta': forms.TextInput(attrs={'pattern': '[a-zA-Zа-яА-Я]+'}),
                   'first_name': forms.TextInput(attrs={'pattern': '[-a-zA-Zа-яА-Я]+'}),
                   'last_name': forms.TextInput(attrs={'pattern': '[-a-zA-Zа-яА-Я]+'}),
                   'otchestvo': forms.TextInput(attrs={'pattern': '[-a-zA-Zа-яА-Я]+'}),
                   'kem_vidan': forms.TextInput(attrs={'pattern': '[-a-zA-Zа-яА-Я]+'}),
                   'birth_place': forms.TextInput(attrs={'pattern': '[-a-zA-Zа-яА-Я]+'}),
                   'address': forms.TextInput(attrs={'pattern': '[-0-9a-zA-Zа-яА-Я]+'}),
                   'mobile_phone': forms.TextInput(attrs={'pattern':
                                                              '^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'}),
                   'pensioner': forms.CheckboxInput,
                   'voenoobyazaniy': forms.CheckboxInput,
                   'job': forms.TextInput(attrs={'pattern': '[-0-9a-zA-Zа-яА-Я]+'}),
                   'position': forms.TextInput(attrs={'pattern': '[-0-9a-zA-Zа-яА-Я]+'}), }
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', ]


class ProfileForm(forms.ModelForm):
    form = BasicForm

    class Meta:
        model = Profile
        exclude = ['user']


class ProfileAdmin(admin.ModelAdmin):
    form = BasicForm


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['profile']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposits
        fields = '__all__'
        exclude = ['profile']
        widgets = {'deposit_type': forms.RadioSelect}


class AccountAdmin(admin.ModelAdmin):
    form = AccountForm


class DepositAdmin(admin.ModelAdmin):
    form = DepositForm
