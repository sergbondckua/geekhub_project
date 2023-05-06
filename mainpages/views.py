from django.views.generic import DetailView

from mainpages.models import StaticPage


class StaticPageView(DetailView):
    """Static page"""

    model = StaticPage
    template_name = "mainpages/static_page.html"
    context_object_name = "page"
    slug_field = "url"
