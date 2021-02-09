from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils import timezone
from . import models
class PagesSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.7

    def items(self):
        return ["home", "about", "programme-list", "event-list", "executive-list", "social-links", "contact", "madarasah-list", "business-list", "history", "project-list", "scholarship-list"]
    
    def location(self, obj):
        return reverse(obj)

class EventSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Event.objects.all()
    
    def location(self, obj: models.Event):
        return obj.get_absolute_url()


class ExecutiveSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Executive.objects.all()
    
    def location(self, obj: models.Executive):
        return obj.get_absolute_url()


class ProgrammeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Programme.objects.all()
    
    def location(self, obj: models.Programme):
        return obj.get_absolute_url()



class BusinessSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Business.objects.all()
    
    def location(self, obj: models.Business):
        return obj.get_absolute_url()



class ProjectSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Project.objects.all()
    
    def location(self, obj: models.Project):
        return obj.get_absolute_url()


class ScholarshipSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return models.Scholarship.objects.all()
    
    def location(self, obj: models.Scholarship):
        return obj.get_absolute_url()