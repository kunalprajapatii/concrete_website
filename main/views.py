from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    services = [
        {'description': "Precision woodwork tailored to your space.", 'icon': 'main/carpentry.png'},
        {'description': "Reliable plumbing solutions when you need them most.", 'icon': 'main/plumbing.png'},
        {'description': "Safe, smart, and seamless electrical services.", 'icon': 'main/electrical.png'},
        {'description': "Add color. Add character. Add value.", 'icon': 'main/painting.png'},
        {'description': "One call for all your fix-it needs.", 'icon': 'main/maintenance.png'}
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )

            try:
                send_mail(
                    subject=f"New Contact Form: {contact.subject or 'No Subject'}",
                    message=f"From: {contact.first_name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['kunalprajapat8447@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                print("Email Error:", e)

            messages.success(request, "Thank you for contacting us!")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'main/home.html', {'form': form, 'services': services})
