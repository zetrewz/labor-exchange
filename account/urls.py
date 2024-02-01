from django.urls import path
from django.views.generic import TemplateView

from account.views import user_logout, Register, EmailVerify, Login, Config

app_name = 'account'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),

    path('login/', Login.as_view(), name='login'),

    path('logout/', user_logout, name='logout'),

    path('confirm_email/',
         TemplateView.as_view(template_name='registration/confirm.html'),
         name='confirm_email'),

    path('verify_email/<uidb64>/<token>/',
         EmailVerify.as_view(),
         name='verify_email'),

    path('invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),

    path('config/', Config.as_view(), name='config')
]
