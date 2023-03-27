"""URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("", views.EventsListView.as_view(), name="events"),
    path(
        "events/<int:pk>/",
        views.EventDetailView.as_view(),
        name="event-detail"
    ),
    path(
        "distance/<int:pk>/",
        views.RegisterAthleteDistanceView.as_view(),
        name="register_athlete_distance"
    ),
    path(
        "results/",
        views.ResultsEventView.as_view(),
        name="results",
    ),
    path(
            "results/<int:pk>/",
            views.ResultsEventDetailView.as_view(),
            name="results-detail",
        ),
]

app_name = "sportevent"
