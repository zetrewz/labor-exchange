from django.urls import path

from chat.views import ChatRoom, ChatPlace

app_name = 'chat'

urlpatterns = [
    path('room/<int:application_id>/', ChatRoom.as_view(), name='chat_room'),

    path('place/', ChatPlace.as_view(), name='chat_place'),
]
