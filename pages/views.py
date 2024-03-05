from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages



class HomePageView(TemplateView):
    template_name = "pages/home.html"
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
      
        return render(request, self.template_name)
    
def home_page_view(request):
    return render(request, 'pages/home.html')


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        messages.success(request, 'Your message has been sent successfully!')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class ServicesPageView(TemplateView):
    template_name = "pages/services.html"

class ClientPageView(TemplateView):
    template_name = "pages/clients.html"

