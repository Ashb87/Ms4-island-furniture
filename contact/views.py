from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import OrderInquiryForm


def order_inquiry(request):
    """ Allow users to send order enquiries """
    user_email = request.POST.get('contact_email')

    if request.method == 'POST':
        inquiry_form = {
            'name': request.POST.get('name'),
            'contact_email': request.POST.get('contact_email'),
            'order_number': request.POST.get('order_number'),
            'message': request.POST.get('message'),
        }
        # send email
        subject = render_to_string(
            'contact/order_inquiry_emails/inquiry_subject.txt',
            {'inquiry': inquiry_form}
        )
        body = render_to_string(
            'contact/order_inquiry_emails/inquiry_body.txt',
            {'inquiry': inquiry_form}
        )
        send_mail(
            subject, body, user_email, [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )
        messages.success(request, 'Inquiry Successfully Sent!')

    form = OrderInquiryForm

    context = {
        'form': form,
        'on_profile_page': True,
        }

    return render(request, 'contact/contact.html')