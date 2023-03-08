"""Views"""
from django.views import generic

from sportevent.models import Event


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
