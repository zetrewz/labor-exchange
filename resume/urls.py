from django.urls import path

from resume.views import ResumeDetailView, ResumeListView, ResumeCreateView, ResumeUpdateView, \
    ResumeDeleteView, ResumeResponsesView, FavoritesResume

app_name = 'resume'

urlpatterns = [
    path('list/', ResumeListView.as_view(), name='list'),

    path('detail/<int:pk>/', ResumeDetailView.as_view(), name='detail'),

    path('create/', ResumeCreateView.as_view(), name='create'),

    path('update/<int:pk>/', ResumeUpdateView.as_view(), name='update'),

    path('delete/<int:pk>/', ResumeDeleteView.as_view(), name='delete'),

    path('responses/', ResumeResponsesView.as_view(), name='responses'),

    path('favorites_resume/', FavoritesResume.as_view(), name='favorites_resume'),
]
