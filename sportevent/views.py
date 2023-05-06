"""Views"""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.utils.translation import gettext_lazy as _

from profiles.models import Athlete
from profiles.forms import AthleteForm
from sportevent import tasks
from sportevent.models import Event, Distance, RegisterDistanceAthlete


class IndexView(generic.TemplateView):
    """Home page"""

    template_name = "sportevent/home.html"


class EventsListView(generic.ListView):
    """List of all events"""

    model = Event
    queryset = Event.objects.filter(registration_end_date__gt=timezone.now()).order_by(
        "date_event"
    )
    paginate_by = 6


class EventDetailView(generic.DetailView):
    """Details of the sports event"""

    model = Event


class RegisterAthleteDistanceView(LoginRequiredMixin, generic.DetailView):
    """Register a new athlete on distance"""

    model = Distance
    form_class = AthleteForm
    login_url = "/accounts/login/"
    template_name = "sportevent/register_distance.html"

    def get_context_data(self, **kwargs) -> dict:
        """Get the details of the sport event/distance and register"""
        context = super().get_context_data(**kwargs)
        if not RegisterDistanceAthlete.objects.filter(
            distance=self.object, athlete=self.request.user
        ).exists():
            initial = (
                {
                    # "username": self.request.user.username,
                    "first_name": self.request.user.first_name,
                    "last_name": self.request.user.last_name,
                    "email": self.request.user.email,
                    "date_of_birth": self.request.user.date_of_birth,
                    "gender": self.request.user.gender,
                    "phone": self.request.user.phone,
                    "city": self.request.user.city,
                    "club": self.request.user.club,
                }
                if not self.request.user.is_anonymous
                else None
            )
            if (
                timezone.now().replace(microsecond=0)
                < self.object.event.registration_end_date
            ):
                context["form"] = AthleteForm(initial=initial)
            else:
                messages.error(
                    self.request,
                    _("Registration date is outside of the allowed period."),
                )
                print(timezone.now().replace(microsecond=0))
                print(self.object.event.registration_end_date)
        return context

    def post(self, request, pk: int) -> redirect:
        """Register athlete on distance and update information form"""
        self.object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            athlete = Athlete.objects.get(pk=request.user.id)
            athlete_form = AthleteForm(form.cleaned_data, instance=athlete)
            athlete_form.save()
            RegisterDistanceAthlete.objects.create(
                athlete=athlete,
                distance=self.object,
            )
            tasks.send_to_athlete.delay(
                athlete_email=form.instance.email,
                distance=f"{self.object.title} {self.object.distance_in_unit}",
                event=self.object.event.title,
            )
            messages.success(request, _("Вітаю! Ви успішно зареєструвалися."))
            return redirect(
                reverse_lazy("sportevent:register_athlete_distance", kwargs={"pk": pk})
            )
        messages.error(request, _("Не вірно введені дані."))
        return redirect(
            reverse_lazy("sportevent:register_athlete_distance", kwargs={"pk": pk})
        )


class ResultsEventDetailView(generic.DetailView):
    """Results event detail view"""

    model = Event
    template_name = "sportevent/results_event_detail.html"


class ResultsEventView(generic.ListView):
    """View for displaying the results of an event"""

    model = Event
    queryset = Event.objects.filter(registration_end_date__lt=timezone.now())
    template_name = "sportevent/results_event_list.html"
    paginate_by = 6
