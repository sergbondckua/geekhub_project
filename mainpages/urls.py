from django.urls import path
from mainpages import views

urlpatterns = [
    path(
        "<slug:slug>/",
        views.StaticPageView.as_view(),
        name="static_page",
    ),
]

app_name = "mainpages"
