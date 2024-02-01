from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, TextField, DateTimeField, CharField, Index, CASCADE

User = get_user_model()


class ChatMessage(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)
    room_group_name = CharField(max_length=255)

    class Meta:
        indexes = [Index(fields=['room_group_name'])]

    def __str__(self):
        return f"{self.room_group_name} {self.user} {self.content}"
