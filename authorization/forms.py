from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from authorization.models import CustomUser, CustomUserManager, Role

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('Пароли не совпадают!'),
        'email_exists': _('Пользователь с таким адресом электронной почты уже существует.'),
        'password_too_short': _('Этот пароль слишком короткий. Он должен содержать не менее 8 символов.')
    }
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное имя.",
            code="invalid_first_name"
        )
    ])
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительную фамилию.",
            code="invalid_last_name"
        )
    ])
    patronymic = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное отчество.",
            code="invalid_patronymic"
        )
    ])
    contacts = forms.CharField(required=True, validators=[
        RegexValidator(  # regular expression for phone number validation
            message="Введите правильный номер телефона.",
            code="invalid_phone_number"
        )
    ], widget=forms.TextInput(attrs={'pattern': r'^\+7(\s+)?\(?7[0-9]{2}\)?(\s+)?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())
    company = forms.CharField(max_length=200, required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.filter(id__in=[1, 2]), required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'contacts', 'password1', 'password2', 'role',
                  'company')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        return email

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        return contacts


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное имя.",
            code="invalid_first_name"
        )
    ])
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительную фамилию.",
            code="invalid_last_name"
        )
    ])
    patronymic = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное отчество.",
            code="invalid_patronymic"
        )
    ])
    contacts = forms.CharField(required=True, validators=[
        RegexValidator(  # regular expression for phone number validation
            message="Введите правильный номер телефона.",
            code="invalid_phone_number"
        )
    ], widget=forms.TextInput(attrs={'pattern': r'^\+7(\s+)?\(?7[0-9]{2}\)?(\s+)?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$'}))
    company = forms.CharField(max_length=200, required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.filter(id__in=[1, 2]), required=True)

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        return contacts


class EditForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное имя.",
            code="invalid_first_name"
        )
    ])
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительную фамилию.",
            code="invalid_last_name"
        )
    ])
    patronymic = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное отчество.",
            code="invalid_patronymic"
        )
    ])
    contacts = forms.CharField(required=True, validators=[
        RegexValidator(  # regular expression for phone number validation
            message="Введите правильный номер телефона.",
            code="invalid_phone_number"
        )
    ], widget=forms.TextInput(attrs={'pattern': r'^\+7(\s+)?\(?7[0-9]{2}\)?(\s+)?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$'}))
    company = forms.CharField(max_length=200, required=True)

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        return contacts


class AdminCreationFrom(UserCreationForm):
    error_messages = {
        'password_mismatch': _('Пароли не совпадают!'),
        'email_exists': _('Пользователь с таким адресом электронной почты уже существует.'),
        'password_common': 'Этот пароль слишком распространен.',
        'password_numeric': 'Этот пароль полностью состоит из чисел.',
        'password_is_too_short': 'Этот пароль слишком короткий. Он должен содержать не менее 8 символов.',
    }
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное имя.",
            code="invalid_first_name"
        )
    ])
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительную фамилию.",
            code="invalid_last_name"
        )
    ])
    patronymic = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Zа-яА-ЯәӘіІңҢғҒүҮұҰқҚөӨһҺ]*$',
            message="Введите действительное отчество.",
            code="invalid_patronymic"
        )
    ])
    contacts = forms.CharField(required=True, validators=[
        RegexValidator(  # regular expression for phone number validation
            message="Введите правильный номер телефона.",
            code="invalid_phone_number"
        )
    ], widget=forms.TextInput(attrs={'pattern': r'^\+7(\s+)?\(?7[0-9]{2}\)?(\s+)?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'contacts', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        return email

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        return contacts

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1.lower() in {'password', '123456', 'qwerty', 'password123'}:
            raise forms.ValidationError(
                self.error_messages['password_common'],
                code='password_common',
            )
        if password1.isdigit():
            raise forms.ValidationError(
                self.error_messages['password_numeric'],
                code='password_numeric',
            )
        if len(password1) < 8:
            raise forms.ValidationError(
                self.error_messages['password_is_too_short'],
                code='password_is_too_short',
            )
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if self.cleaned_data.get('password1') and password2 and self.cleaned_data.get('password1') != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        return password2


class PasswordReset(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))


class PasswordResetConfirm(forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    error_messages = {
        'password_common': 'Этот пароль слишком распространен.',
        'password_numeric': 'Этот пароль полностью состоит из чисел.',
        'password_is_too_short': 'Этот пароль слишком короткий. Он должен содержать не менее 8 символов.',
        'password_mismatch': 'Два пароля не совпадают.',
    }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1.lower() in {'password', '123456', 'qwerty', 'password123'}:
            raise forms.ValidationError(
                self.error_messages['password_common'],
                code='password_common',
            )
        if password1.isdigit():
            raise forms.ValidationError(
                self.error_messages['password_numeric'],
                code='password_numeric',
            )
        if len(password1) < 8:
            raise forms.ValidationError(
                self.error_messages['password_is_too_short'],
                code='password_is_too_short',
            )
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if self.cleaned_data.get('password1') and password2 and self.cleaned_data.get('password1') != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        return password2
