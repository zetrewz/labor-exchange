from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from service.models import Application
from service.utils import get_vacancy_pks
from vacancy.forms import VacancyCreateForm
from vacancy.models import Vacancy


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy_list = context['vacancies']
        paginator = Paginator(vacancy_list, 8)
        page_number = self.request.GET.get('page', 1)

        try:
            vacancies = paginator.page(page_number)
        except EmptyPage:
            vacancies = paginator.page(paginator.num_pages)
        context['vacancies'] = vacancies

        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy/detail.html'
    context_object_name = 'vacancy'


class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = VacancyCreateForm
    template_name = 'vacancy/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('vacancy:list')


class VacancyUpdateView(UpdateView):
    model = Vacancy
    form_class = VacancyCreateForm
    template_name = 'vacancy/update.html'

    def get_success_url(self):
        return reverse_lazy('vacancy:list')


class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancy/delete.html'
    success_url = reverse_lazy('vacancy:list')


class VacancyResponsesView(ListView):
    model = Application
    template_name = 'vacancy/responses.html'
    context_object_name = 'responses'

    def get_queryset(self):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])

        return Application.objects.filter(vacancy=vacancy)


class FavoritesVacancy(ListView):
    model = Vacancy
    template_name = 'vacancy/favorites_vacancy.html'
    context_object_name = 'favorite_vacancy'

    def get_queryset(self):
        return self.request.user.favorites_vacancy.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy_pks = get_vacancy_pks(self.request.user, context['favorite_vacancy'])
        context['vacancy_pks'] = vacancy_pks

        return context

