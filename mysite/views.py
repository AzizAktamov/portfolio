from django.shortcuts import render,HttpResponseRedirect
from .models import About,Portfolio
from .bot import send_message
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def home_view(requst):
    return render(request=requst,template_name="index.html")

def about_view(requst):
    abouts = About.objects.all()
    context = {"abouts":abouts}
    return render(requst, 'about.html',context)

def do_view(requst):
    return render(request=requst,template_name="do.html")

def portfolio_view(requst):
    portfolios = Portfolio.objects.all()
    context = {"portfolios":portfolios}
    return render(requst, "portfolio.html",context)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]              
            phone_numer = form.cleaned_data["phone_numer"]  # Corrected this line
            description = form.cleaned_data["description"]
        

            send_message(name,email ,phone_numer , description )

            form = ContactForm()  # Reset the form after successful submission
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...')
            return HttpResponseRedirect(reverse('contact-page'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
