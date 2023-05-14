from django.contrib import admin
from django.urls import path, include

from direct.views import inbox, Directs, SendDirect, UserSearch, NewConversation

urlpatterns = [
    path('', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),
]
