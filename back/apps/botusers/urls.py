from django.urls import path
from .views import BotUserCreateView

urlpatterns = [
    path('create/', BotUserCreateView.as_view(), name='bot-user-create'),
]