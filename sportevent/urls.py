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
]

app_name = "sportevent"
