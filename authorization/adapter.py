from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return 'complete_registration'

    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed.
        """
        print("pastala")
        # If the user is logging in with Google and hasn't registered before,
        # redirect them to a registration page
        if sociallogin.account.provider == 'google' and not sociallogin.user.patronymic:
            return redirect(reverse('polls:complete_registration'))

        # If the user has already registered, proceed with login
        return super().pre_social_login(request, sociallogin)


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        user.email = sociallogin.account.user.email
        user.is_email_verified = True
        user.save()
        return user
