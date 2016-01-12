from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class FetchView(View):
    def post(self, request, *args, **kwargs):
        url = self.request.POST.get('url','')
        return render(request, 'parmeter.html')

class LaunchView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'launchva.html')



