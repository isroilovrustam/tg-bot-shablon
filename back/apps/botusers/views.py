from rest_framework import generics
from .models import BotUser
from .serializers import BotUserSerializer

class BotUserCreateView(generics.CreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer