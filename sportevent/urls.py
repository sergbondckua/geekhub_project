from django.urls import path
from sportevent import views

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("", views.EventsListView.as_view(), name="events"),
    path("event/<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
    path(
        "distance/<int:pk>/",
        views.RegisterAthleteDistanceView.as_view(),
        name="register_athlete_distance",
    ),
    path(
        "event/results/",
        views.ResultsEventView.as_view(),
        name="results",
    ),
    path(
        "event/<int:pk>/result",
        views.ResultsEventDetailView.as_view(),
        name="results-detail",
    ),
]

app_name = "sportevent"
