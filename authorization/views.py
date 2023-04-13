from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from invtech.models import invtech_info
from entry_app.models import temp_invtech_info

import os

from authorization.models import CustomUser, Role
from .forms import CustomUserCreationForm, CustomUserLoginForm, PasswordReset, PasswordResetConfirm, RegistrationForm, \
    AdminCreationFrom, EditForm


class IndexView(generic.ListView):
    model = CustomUser
    template_name = 'polls/index.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invtechs = invtech_info.objects.all()
        temp_invtechs = temp_invtech_info.objects.all()
        context = {
            'invtechs': invtechs,
            'temp_invtechs': temp_invtechs,
        }
        return context


def mypublication(request):
    ppit_id1 = request.COOKIES.get('ppit_id1')
    print('ppit_id1 = ', ppit_id1)
    invtechs = invtech_info.objects.filter(it_id=ppit_id1)
    filename = invtech_info.objects.filter(it_id=ppit_id1).values_list('full_hars', flat=True)[0]
    itfile = invtech_info.objects.filter(it_id=ppit_id1).values_list('invtech', flat=True)[0]
    pdffile = '/static/files/invtech_files/' + itfile + '/' + filename
    #print(pdffile)
    images = invtechs.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/files/invtech_files/' + itfile + '/' + image_list[i]
            image_list[i] = image

    context = {
        'invtechs': invtechs,
        'image_list': image_list,
        'pdffile': pdffile,
    }
    return render(request, 'polls/my_publication.html', context)


def myapplication(request):
    pptit_id1 = request.COOKIES.get('pptit_id1')
    temp_invtechs = temp_invtech_info.objects.filter(it_id=pptit_id1)
    filename = temp_invtech_info.objects.filter(it_id=pptit_id1).values_list('full_hars', flat=True)[0]
    itfile = temp_invtech_info.objects.filter(it_id=pptit_id1).values_list('invtech', flat=True)[0]
    pdffile = '/static/uploads/invtech_files/' + itfile + '/' + filename
    #print(pdffile)
    images = temp_invtechs.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/uploads/invtech_files/' + itfile + '/' + image_list[i]
            image_list[i] = image

    context = {
        'temp_invtechs': temp_invtechs,
        'image_list': image_list,
        'pdffile': pdffile,
    }
    return render(request, 'polls/my_application.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False  # set email verification to false
            user.role = form.cleaned_data['role']
            user.save()
            subject = 'Активируйте ваш аккаунт'
            message = f'Привет {user.first_name} {user.last_name},\n\n' \
                      f'Пожалуйста, нажмите на ссылку ниже, чтобы подтвердить свой адрес электронной почты:\n' \
                      f'{request.build_absolute_uri(reverse("polls:verify_email", args=[user.token]))}\n\n'
            from_email = 'Aitkazinn03@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'polls/register_done.html')
        else:
            print("form is invalid")
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})


def verify_email(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_email_verified = True
    user.is_active = True  # set user as active
    user.save()
    return render(request, 'polls/verify_email_done.html')


@login_required
def complete_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.patronymic = form.cleaned_data['patronymic']
            user.contacts = form.cleaned_data['contacts']
            user.company = form.cleaned_data['company']
            user.role = form.cleaned_data['role']
            user.save()
            # Redirect the user to the next page
            return redirect('polls:profile')
    else:
        form = RegistrationForm()

    return render(request, 'polls/complete_registration.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None and user.is_email_verified and user.is_active:
                login(request, user)
                return redirect('polls:profile')
            else:
                print(form.errors)
                form.add_error(None, 'Неверный адрес электронной почты или пароль')
    else:
        form = CustomUserLoginForm()
    return render(request, 'polls/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('polls:profile')


def password_reset(request):
    if request.method == 'POST':
        form = PasswordReset(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = get_object_or_404(CustomUser, email=email)
            subject = 'Востановление пароля'
            message = f'Здравствуйте {email},\n\n' \
                      f'Вы получили это электронное письмо, потому что запросили сброс пароля для своей учетной записи пользователя по сайту QazJolGZI.\n' \
                      f'Перейдите на следующую страницу и выберите новый пароль:\n' \
                      f'{request.build_absolute_uri(reverse("polls:password_reset_confirm", args=[user.token]))}\n\n'
            from_email = 'Aitkazinn03@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('polls:password_reset_done')
    else:
        form = PasswordReset()

    return render(request, 'polls/password_reset.html', {'form': form})


def password_reset_done(request):
    return render(request, 'polls/password_reset_done.html')


def password_reset_confirm(request, token):
    if request.method == 'POST':
        form = PasswordResetConfirm(request.POST)
        if form.is_valid():
            user = get_object_or_404(CustomUser, token=token)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect('polls:password_reset_complete')
    else:
        form = PasswordResetConfirm()

    return render(request, 'polls/password_reset_confirm.html', {'form': form})


def password_reset_complete(request):
    return render(request, 'polls/password_reset_complete.html')


def list_admin(request):
    user = get_user_model()
    admins = user.objects.filter(role=3)
    role = 3
    context = {
        "admins": admins,
        "role": role
    }
    return render(request, 'polls/admin_page.html', context)


def list_projector(request):
    user = get_user_model()
    admins = user.objects.filter(role=1)
    role = 1
    context = {
        "admins": admins,
        "role": role
    }
    return render(request, 'polls/admin_page.html', context)


def list_provider(request):
    user = get_user_model()
    admins = user.objects.filter(role=2)
    role = 2
    context = {
        "admins": admins,
        "role": role
    }
    return render(request, 'polls/admin_page.html', context)


def create_user(request):
    if request.method == 'POST':
        form = AdminCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = True  # set email verification
            user.is_admin = True
            user.role = Role.objects.filter(id=3).first()
            user.save()
            return redirect('polls:profile')
    else:
        form = AdminCreationFrom()

    return render(request, 'polls/admin_creation.html', {'form': form})


def delete_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        try:
            user = User.objects.get(email=email, first_name=first_name)
            user.delete()
            return redirect('polls:profile')
        except User.DoesNotExist:
            return render(request, 'polls/user_delete.html', {'error': 'User does not exist.'})
    return render(request, 'polls/user_delete.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.patronymic = form.cleaned_data['patronymic']
            user.contacts = form.cleaned_data['contacts']
            user.company = form.cleaned_data['company']
            user.save()
            return redirect('polls:profile')
    else:
        form = EditForm()

    return render(request, 'polls/edit_profile.html', {'form': form})



User = get_user_model()


