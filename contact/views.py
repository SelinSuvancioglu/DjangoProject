from django.http import JsonResponse
from django.shortcuts import render, redirect


from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def contact_form(request):
    if request.method == 'POST':
        nameText = request.POST['name']
        emailText = request.POST['email']
        subjectText = request.POST['subject']
        messageText = request.POST['message']

        send_mail(
            subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['suvanciogluselin@gmail.com'],  # Alıcı e-posta adresi

        )

        print("if worked")
        return render(request, 'contact.html', {"message_name": nameText})
    else:

        print("else worked")
        return render(request, 'contact.html', {"message_name": "sa"})

def contact(request):
    return render(request, 'contact.html')

# forms.py




