from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from project_movie.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def register(request):
    form=RegistrationForm()
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            messages.success(request, f'Welcome {first_name} {last_name}, your account has been created successfully!')
            user=form.save(commit=False)
            user.is_active = False
            user.save()
            current_site=get_current_site(request)
            mail_subject="Activate your account"
            message=render_to_string("users/account_activation_email.html", {"user":user,
                                                             "domain":current_site.domain,
                                                             "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                                                             "token":account_activation_token.make_token(user),
                                                             })
            to_email=form.cleaned_data.get("email")
            email=EmailMessage(mail_subject, message, to=[to_email])
            sent_count=email.send()
            messages.success(request, "A confirmation link has been sent to your email: {email}. Please check your inbox to complete the registration!")
            return redirect("register")
    return render(request, "users/register.html", {"form":form})

def activate(request, uidb64, token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        login(request, user)
        messages.success(request, "Your account has been activated successfully!")
        return redirect(reverse("index"))
    else:
        messages.error(request, "Activation link is invalid or expired!")
        return redirect("index")

@login_required
def profile(request):
    user_profile=Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {"profile":user_profile})