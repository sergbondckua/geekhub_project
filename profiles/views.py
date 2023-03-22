""" Views profiles """
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from profiles.forms import AthleteForm
from profiles.models import Athlete


class ProfileView(DetailView):
    """ View profile """
    model = Athlete

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Views update profiles """
    model = Athlete
    form_class = AthleteForm
    success_message = _("Дані вашого профілю змінено")
    success_url = reverse_lazy("profiles:profile_update")

    def get_object(self):
        return self.request.user


class AthleteDistancesRegister(LoginRequiredMixin, ListView):
    """ View all distances of a athlete """
    model = Athlete
    context_object_name = "athlete_distances_list"
    template_name = "profiles/athlete_distances_list.html"

    def get_queryset(self):
        queryset = Athlete.objects.get(
            id=self.request.user.id).registered_distance.all()
        return queryset
