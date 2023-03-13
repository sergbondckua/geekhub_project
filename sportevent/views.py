"""Views"""
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.utils.translation import gettext_lazy as _

from sportevent.forms import AthleteForm
from sportevent.models import Event, Distance, RegisterDistanceAthlete, Athlete


class IndexView(generic.TemplateView):
    """ Home page """
    template_name = "sportevent/home.html"


class EventsListView(generic.ListView):
    """ List of all events """
    model = Event
    paginate_by = 6


class EventDetailView(generic.DetailView):
    """ Details of the sports event """
    model = Event


class RegisterAthleteDistanceView(generic.View):
    """ Register a new athlete on distance """
    model = Distance
    form_class = AthleteForm
    template_name = "sportevent/register_distance.html"

    # def get_context_data(self, **kwargs) -> dict:
    #     """ Get the details of the sport event/distance and register"""
    #     context = super().get_context_data(**kwargs)
    #     initial = {
    #         "first_name": self.request.user.first_name,
    #         "last_name": self.request.user.last_name,
    #         "email": self.request.user.email,
    #         "date_of_birth": self.request.user.date_of_birth,
    #         "gender": self.request.user.gender,
    #         "phone": self.request.user.phone,
    #         "city": self.request.user.city,
    #         "club": self.request.user.club,
    #     } if not self.request.user.is_anonymous else None
    #     context["form"] = self.form_class(initial=initial)
    #     return context

    def post(self, request, pk: int) -> redirect:
        """Register"""
        distance = self.model.objects.get(id=pk)
        form = self.form_class(request.POST)

        if not RegisterDistanceAthlete.objects.filter(distance_id=pk).filter(
                athlete_id=request.user.id).exists():
            if form.is_valid():
                athlete = Athlete.objects.get(pk=request.user.id)
                athlete_form = self.form_class(
                    form.cleaned_data, instance=athlete)
                athlete_form.save()
                RegisterDistanceAthlete.objects.create(
                    athlete=athlete,
                    distance=distance,
                )
                messages.success(
                    request, _("Вітаю! Ви успішно зареєструвалися."))
                return redirect(
                    reverse_lazy('sportevent:event-detail',
                                 kwargs={"pk": distance.event.id}))
        messages.error(
            request, _("Ви раніше вже реєструвалися на цю дистанцію."))
        return redirect(
            reverse_lazy('sportevent:event-detail',
                         kwargs={"pk": distance.event.id}))

    def get(self, request, pk):
        """Get the distance event"""
        distance = self.model.objects.get(id=pk)
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": self.request.user.email,
            "date_of_birth": request.user.date_of_birth,
            "gender": request.user.gender,
            "phone": request.user.phone,
            "city": request.user.city,
            "club": request.user.club,
        } if not request.user.is_anonymous else None
        form = self.form_class(initial=initial)
        context = {"distance": distance, "form": form}
        return render(request, self.template_name, context=context)
