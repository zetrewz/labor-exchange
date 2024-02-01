from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from django.core.cache import cache
from django.db.models import Q

from resume.models import Resume
from service.models import Application
from vacancy.models import Vacancy


def is_employer(user):
    return hasattr(user, 'profile')


def is_worker(user):
    return not hasattr(user, 'profile')


def get_vacancy_pks(user, results):
    vacancy_pks = [vacancy.pk for vacancy in results]
    applications = Application.objects.filter(
        resume__user=user,
        vacancy_id__in=vacancy_pks
    ).values_list('vacancy_id', flat=True)
    return applications


def get_search_resumes(search_vector, query):
    results = (
        Resume.objects
        .annotate(rank=SearchRank(search_vector, SearchQuery(query)))
        .filter(Q(work_name__icontains=query) | Q(work_name__iregex=query))
        .order_by('-rank')
    )
    return results


def get_search_vacancies(search_vector, query):
    results = (
        Vacancy.published
        .annotate(rank=SearchRank(search_vector, SearchQuery(query)))
        .filter(Q(name__icontains=query) | Q(name__iregex=query))
        .order_by('-rank')
    )
    return results


def get_rec_resumes(name):
    rec_resumes = (Resume.objects
                   .annotate(rank=SearchRank(SearchVector('work_name'), SearchQuery(name)))
                   .filter(Q(work_name__icontains=name) | Q(work_name__iregex=name))
                   .order_by('-rank'))[:6]
    return rec_resumes


def get_rec_vacancy(work_name):
    rec_vacancy = (Vacancy.published
                   .annotate(rank=SearchRank(SearchVector('name'), SearchQuery(work_name)))
                   .filter(Q(name__icontains=work_name) | Q(name__iregex=work_name))
                   .order_by('-rank'))[:6]
    return rec_vacancy


def perform_search(query, user):
    if is_employer(user):
        return search_resumes(query), []
    elif hasattr(user, 'resume'):
        return search_vacancies(query, user)
    else:
        return Vacancy.published.all(), []


def search_resumes(query):
    cache_key = f"search_resumes_{query}"
    cached_result = cache.get(cache_key)

    if cached_result is not None:
        return cached_result

    search_vector = SearchVector('work_name', weight='A') + \
                    SearchVector('experience', weight='B') + \
                    SearchVector('about', weight='D')
    results = get_search_resumes(search_vector, query)

    cache.set(cache_key, results, timeout=3600)
    return results


def search_vacancies(query, user):
    search_vector = SearchVector('name', weight='A') + \
                    SearchVector('responsibilities', weight='B') + \
                    SearchVector('requirements', weight='B')
    results = get_search_vacancies(search_vector, query)

    vacancy_pks = get_vacancy_pks(user, results)

    return results, vacancy_pks
