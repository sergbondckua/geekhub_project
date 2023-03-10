"""Views"""
from django.shortcuts import render
from django.views import generic

from sportevent.models import Event, Distance


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

    def get(self, request, pk):
        """Get the distance event"""
        distance = Distance.objects.get(id=pk)
        athlete = request.user
        distance.athlete.add(athlete)
        return render(request,
                      "sportevent/distance_form.html",
                      {"distance": distance, "athlete": athlete})
