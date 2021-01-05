from django.views.generic import TemplateView
from typing import Dict, Any
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