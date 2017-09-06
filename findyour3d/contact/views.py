from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        context = {}
        feedback_form = ContactForm(request.POST)
        context["form"] = feedback_form
        if feedback_form.is_valid():
            feedback_form.save()
            response = redirect('home')
            response['Location'] += '?message_sent=success'
            return response
        else:
            return render(request, 'pages/home.html', context)
    else:
        return render(request, 'pages/home.html')
