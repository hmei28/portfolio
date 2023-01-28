from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Experience, Formation, PersoInformation, Skill
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'resume/index.html', context={"experience": Experience.objects.all(),
                                                       "formation": Formation.objects.all(),
                                                       "perso_info": PersoInformation.objects.all(),
                                                       "skill": Skill.format_skills(),
                                                       "form": form
                                                       })
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email_from = settings.EMAIL_HOST_USER
            email_to = settings.DEFAULT_EMAIL_RECIPIENT.split(',')
            contact = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            format_message = f"{message}\n\nContact : {contact}"
            try:
                send_mail(subject, format_message, email_from, email_to)
                messages.success(request, 'Mail is sent successfully :)')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
                messages.error(request, 'Invalid form submission.')
        return HttpResponseRedirect(reverse('resume-index') + '#contact')