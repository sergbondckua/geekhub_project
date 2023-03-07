from django.shortcuts import render
from django.views import generic

from sportevent.models import Event


class IndexView(generic.TemplateView):
    """Головна сторінка"""
    template_name = "sportevent/home.html"


class EventsListView(generic.ListView):
    """Список всіх заходів"""
    model = Event
    paginate_by = 12


class EventDetailView(generic.DetailView):
    """Подробиці спорт заходу"""
    model = Event
