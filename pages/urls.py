from django.urls import path

from .views import BusinessDetailView, BusinessListView, ContactView, EventListView,EventDetailView, ExecutiveDetailView, ExecutiveListView, HistoryView, HomePageView, AboutPageView, MadarasahListView, ProgrammeDetailView, ProgrammeListView, ProjectListView, ScholarshipDetailView, ScholarshipListView, SocialLinksView, upload_event_images, ProjectDetailView

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
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("madarasah/", MadarasahListView.as_view(), name="madarasah-list"),

    path("business/", BusinessListView.as_view(), name="business-list"),
    path("business/<slug:slug>/", BusinessDetailView.as_view(), name="business-detail"),
    path("history/", HistoryView.as_view(), name="history"),

    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("scholarships/", ScholarshipListView.as_view(), name="scholarship-list"),
    path("scholarships/<int:pk>", ScholarshipDetailView.as_view(), name="scholarship-detail"),
]
