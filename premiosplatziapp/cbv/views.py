from django.shortcuts import render

from django.views.generic import TemplateView, RedirectView

from polls.models import Question, Choice

# Create your views here.
class ExampleTemplateView(TemplateView):
    template_name='cbv/template_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Gryffindor'
        context['data'] = 'Context for the example'
        return context
    
class ExampleRedirectView(RedirectView):
    url = 'https://www.youtube.com/watch?v=5a2eFo8-xbk'