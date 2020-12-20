from django.shortcuts import render
from django.views import View

# Create your views here.


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'user': {'is_logged': None}})


class MainView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class CategoriesView(View):
    def get(self, request):
        return render(request, 'categories.html')


class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html')
