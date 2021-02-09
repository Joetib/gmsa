from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import BusinessSitemap, EventSitemap, ExecutiveSitemap, PagesSiteMap, ProgrammeSitemap, ProjectSitemap, ScholarshipSitemap 
sitemaps = {
    "pages": PagesSiteMap,
    "events": EventSitemap,
    "executives": ExecutiveSitemap,
    "programmes": ProgrammeSitemap,
    "businesses": BusinessSitemap,
    "projects": ProjectSitemap,
    "scholarships": ScholarshipSitemap
}

urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

