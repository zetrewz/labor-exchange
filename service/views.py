from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.views import View

from resume.models import Resume
from service.forms import SearchForm
from service.utils import is_worker, get_vacancy_pks, perform_search, get_rec_resumes, get_rec_vacancy
from vacancy.models import Vacancy


class Search(View):
    def get(self, request):
        query = request.GET.get('query')
        results = []
        vacancy_pks = []
        user = request.user

        form = SearchForm(request.GET)
        if form.is_valid():
            search_results, vacancy_pks = perform_search(query, user)
            paginator = Paginator(search_results, 8)
            page_number = request.GET.get('page', 1)

            try:
                results = paginator.page(page_number)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)

        context = {
            'query': query,
            'results': results,
            'vacancy_pks': vacancy_pks,
        }

        return render(request, 'service/search.html', context)


class Feed(View):
    def get(self, request):
        user = request.user
        vacancy_pks = []
        rec_vacancy = []
        rec_resumes = []

        try:
            if is_worker(user):
                rec_vacancy_cache_key = f"rec_vacancy_{user.id}"
                rec_vacancy = cache.get(rec_vacancy_cache_key)

                if rec_vacancy is None:
                    work_name = user.resume.work_name
                    rec_vacancy = get_rec_vacancy(work_name)

                    if not rec_vacancy.exists():
                        rec_vacancy = Vacancy.published.all()[:6]

                    cache.set(rec_vacancy_cache_key, rec_vacancy, timeout=3600)

                vacancy_pks = get_vacancy_pks(user, rec_vacancy)

            else:
                rec_resumes_cache_key = f"rec_resumes_{user.id}"
                rec_resumes = cache.get(rec_resumes_cache_key)

                if not rec_resumes:
                    if user.vacancies.exists():
                        name = user.vacancies.last().name
                        rec_resumes = get_rec_resumes(name)

                        if not rec_resumes.exists():
                            rec_resumes = Resume.objects.all()[:6]

                        cache.set(rec_resumes_cache_key, rec_resumes, timeout=3600)
        except:
            rec_vacancy = Vacancy.published.all()[:6]

        context = {
            'rec_vacancy': rec_vacancy,
            'rec_resumes': rec_resumes,
            'vacancy_pks': vacancy_pks,
        }
        return render(request, 'base.html', context)
