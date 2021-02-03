from django.views.generic import TemplateView, ListView, DetailView, View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import Dict, Any
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from . import forms
from . import models

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['executives'] = models.Executive.objects.filter(is_active=True)
        context['upcoming_events'] = models.Event.objects.filter(is_upcoming=True)
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["executives"] = models.Executive.objects.filter(is_active=True)
        context["images"] = models.Image.objects.all()
        return context

class ExecutiveListView(ListView):
    model = models.Executive
    context_object_name = "executives"
    template_name = "pages/executive_list.html"

class ExecutiveDetailView(DetailView):
    model = models.Executive
    context_object_name = "executive"
    template_name = "pages/executive_detail.html"
    
class ProgrammeListView(ListView):
    model = models.Programme
    context_object_name = "programmes"
    template_name = "pages/programme_list.html"

class ProgrammeDetailView(DetailView):
    model = models.Programme
    template_name = "pages/programme_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
    
        return context

class EventListView(ListView):
    model = models.Event
    context_object_name = "events"
    template_name = "pages/event_list.html"

class EventDetailView(DetailView):
    model = models.Event
    context_object_name = "event"
    template_name = "pages/event_detail.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["image_form"] = forms.ImageUploadForm()
        return context

@login_required
def upload_event_images(request: HttpRequest, pk:int) -> HttpRequest:
    event = get_object_or_404(models.Event, pk=pk)
    if not request.user.is_superuser:
        return redirect(event.get_absolute_url())
    if request.method == "POST":
        image_form = forms.ImageUploadForm(request.POST, files=request.FILES)
        if image_form.is_valid():
            d = image_form.cleaned_data
            for image in request.FILES.getlist('image'):
                models.Image.for_model(image=image, description=d["description"], content_object=event)
            
    return redirect(event.get_absolute_url())


class SocialLinksView(TemplateView):
    template_name = "pages/social_links.html"        

class ContactView(TemplateView):
    template_name = "pages/contact.html"

    def post(self, request, *args, **kwargs):
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, "Your input has been recorded")
        else:
            messages.error(request, "Sorry there was an error in your form. Please fix and try again.")
        return self.get(request, *args, **kwargs)

class MadarasahListView(ListView):
    model = models.Madarasah
    queryset  = models.Madarasah.objects.all()
    category = None
    search_query = None
    template_name = "pages/madarasah_list.html"
    context_object_name = "madarasah_set"

    def get_queryset(self):
        category_pk = self.request.GET.get('category')
        if category_pk:
            self.category = get_object_or_404(models.MadarasahCategory, pk=int(category_pk))
            queryset = models.Madarasah.objects.filter(category=(self.category))
        else:
            queryset = models.Madarasah.objects.all()
        self.search_query = self.request.GET.get("search")
        if self.search_query:
            queryset = queryset.filter(title__icontains=self.search_query)
        return queryset


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context["category"] = self.category
        context["search"] = self.search_query or ""
        context["categories"] = models.MadarasahCategory.objects.all()
        return context


class BusinessListView(ListView):
    model = models.Business
    context_object_name= "businesses"
    template_name = "pages/business_list.html"

class BusinessDetailView(DetailView):
    model = models.Business
    template_name = "pages/business_detail.html"
    context_object_name = "business"

class HistoryView(TemplateView):
    template_name = "pages/history.html"