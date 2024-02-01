from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from resume.models import Resume
from vacancy.models import Vacancy


def toggle_favorite(model, request, pk):
    obj = get_object_or_404(model, pk=pk)

    if request.user in obj.in_favorites.all():
        obj.in_favorites.remove(request.user)
        return JsonResponse({'status': 'removed'})
    else:
        obj.in_favorites.add(request.user)
        return JsonResponse({'status': 'applied'})


def check_in_favorites(model, request, pk):
    obj = model.objects.filter(pk=pk)

    return JsonResponse({'applied': request.user in obj.in_favorites.all()})


def add_or_remove_favorite(request, pk, type):
    model = Resume if type == 'resume' else Vacancy
    return toggle_favorite(model, request, pk)


def check_favorite_status(request, pk, type):
    model = Resume if type == 'resume' else Vacancy
    return check_in_favorites(model, request, pk)
