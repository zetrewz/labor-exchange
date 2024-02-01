from django.urls import path

from vacancy.views import VacancyCreateView, VacancyListView, VacancyDetailView, VacancyUpdateView, VacancyDeleteView, \
    VacancyResponsesView, FavoritesVacancy

app_name = 'vacancy'

urlpatterns = [
    path('list/', VacancyListView.as_view(), name='list'),
    path('detail/<int:pk>/', VacancyDetailView.as_view(), name='detail'),
    path('create/', VacancyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', VacancyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', VacancyDeleteView.as_view(), name='delete'),
    path('responses/<int:pk>/', VacancyResponsesView.as_view(), name='responses'),
    path('favorites_vacancy/', FavoritesVacancy.as_view(), name='favorites_vacancy'),
]
