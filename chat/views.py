from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.views import View

from chat.models import ChatMessage
from service.models import Application
from service.utils import is_worker

User = get_user_model()


class ChatRoom(View):
    def get(self, request, application_id):
        application = get_object_or_404(Application.objects.select_related(
            'vacancy__user', 'resume__user').only(
            'resume__user__username', 'vacancy__user__username'), id=application_id)

        users_in_chat = [application.vacancy.user_id, application.resume.user_id]

        messages = ChatMessage.objects.filter(
            user_id__in=users_in_chat,
            room_group_name=f'chat_{application.id}'
        ).select_related('user').only(
            'content', 'timestamp', 'room_group_name',
            'user__username'
        )
        context = {'application': application, 'messages': messages}

        return render(request, 'chat/chat_room.html', context)


class ChatPlace(View):
    def get(self, request):
        if is_worker(request.user):
            applications = Application.objects.filter(
                resume__user=request.user
            ).select_related('vacancy')
        else:
            applications = Application.objects.filter(
                vacancy__user=request.user
            ).select_related('resume')
        context = {'applications': applications}

        return render(request, 'chat/chat_place.html', context)
