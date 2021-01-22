from django.urls import path

from .views import EventListView,EventDetailView, ExecutiveDetailView, ExecutiveListView, HomePageView, AboutPageView, ProgrammeDetailView, ProgrammeListView, SocialLinksView, upload_event_images

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('academic-materials/', ProgrammeListView.as_view(), name='programme-list'),
    path('academic-materials/programme/<int:pk>/', ProgrammeDetailView.as_view(), name='programme-detail'),
    path("events/", EventListView.as_view(), name="event-list"),
    path("events/<int:pk>", EventDetailView.as_view(), name="event-detail"),
    path("events/<int:pk>/upload-image/", upload_event_images, name="upload-event-images"),
    path("executives/", ExecutiveListView.as_view(), name="executive-list"),
    path("executives/<int:pk>/", ExecutiveDetailView.as_view(), name="executive-detail"),
    path("social-links/", SocialLinksView.as_view(), name="social-links"),
]
