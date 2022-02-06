""" imports needed for contact views """
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'query': request.POST['query'],
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            user_contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                user_contact.user = user
            user_contact.save()
            send_confirmation_email(user_contact)
            messages.success(request, "Thanks for you message, you should recieve a \
                confirmaion email. We will get \
                back to you as quickly as we can")
            return redirect(reverse('home'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'first_name': profile.default_first_name,
                    'surname': profile.default_surname,
                    'email': profile.default_email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
        template = 'contact/contact.html'
        context = {
            'contact_form': contact_form
        }
        return render(request, template, context)


def send_confirmation_email(user_contact):
    """Send the user a confirmation email"""
    cust_email = user_contact.email
    subject = 'Thank you for contacting Island Furniture'
    body = render_to_string(
            'contact/confirmation_emails/confirmation_email_body.txt',
            {'contact': user_contact})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
