from django.urls import path
from .views import chat_view,getResponse

urlpatterns = [
    path('', chat_view, name='chat'),
    path('getResponse',getResponse, name='getResponse')
]

