""" URL's profile """
from django.urls import path
from . import views

urlpatterns = [
    path("accounts/profile/", views.ProfileView.as_view(), name="profile_view"),
    path(
        "accounts/profile/edit/",
        views.ProfileUpdateView.as_view(),
        name="profile_update",
    ),
    path(
        "accounts/profile/races/",
        views.AthleteDistancesRegister.as_view(),
        name="athlete_distances_register",
    ),
]

app_name = "profiles"
