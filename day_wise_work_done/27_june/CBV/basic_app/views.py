from django.shortcuts import render
from django.views.generic import View,TemplateView
# from django.http import HttpResponse

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based view is cool")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context