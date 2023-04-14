""" Views profiles """
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, ListView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from profiles.forms import AthleteForm


class ProfileView(DetailView):
    """ View profile """
    model = get_user_model()

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Views update profiles """
    model = get_user_model()
    form_class = AthleteForm
    success_message = _("Дані вашого профілю змінено")
    success_url = reverse_lazy("profiles:profile_update")

    def get_object(self):
        return self.request.user


class AthleteDistancesRegister(LoginRequiredMixin, ListView):
    """ View all distances of a athlete """
    model = get_user_model()
    context_object_name = "athlete_distances_list"
    template_name = "profiles/athlete_distances_list.html"

    def get_queryset(self):
        queryset = self.model.objects.get(
            id=self.request.user.id).registered_distance.all().filter(
            distance__event__date_event__gt=timezone.now()).order_by(
            "distance__event__date_event")
        return queryset

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get a context."""
        context = super().get_context_data(**kwargs)
        context["past_events"] = self.model.objects.get(
            id=self.request.user.id).registered_distance.all().filter(
            distance__event__date_event__lt=timezone.now()).order_by(
            "distance__event__date_event")
        return context
